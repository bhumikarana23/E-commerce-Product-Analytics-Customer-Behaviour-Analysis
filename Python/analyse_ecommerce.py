"""
E-commerce Product Analytics & Customer Behaviour Analysis
Run from the project root after extracting the dataset ZIP:
    pip install -r requirements.txt
    python python/analyse_ecommerce.py --data-dir ecommerce_product_analytics_dataset

Outputs are saved to outputs/.
Dataset is synthetic and is not actual Myntra data.
"""
from pathlib import Path
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILES = ["customers", "products", "events", "orders", "order_items"]

def load_data(data_dir: Path):
    data = {}
    for name in FILES:
        path = data_dir / f"{name}.csv"
        if not path.exists():
            raise FileNotFoundError(f"Missing {path}. Extract the dataset ZIP and pass its folder with --data-dir.")
        data[name] = pd.read_csv(path)
    data["events"]["event_timestamp"] = pd.to_datetime(data["events"]["event_timestamp"], errors="coerce")
    data["orders"]["order_date"] = pd.to_datetime(data["orders"]["order_date"], errors="coerce")
    return data

def save_table(df, name, out):
    df.to_csv(out / f"{name}.csv", index=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="ecommerce_product_analytics_dataset")
    parser.add_argument("--output-dir", default="outputs")
    args = parser.parse_args()
    data_dir, out = Path(args.data_dir), Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = load_data(data_dir)
    customers, products, events, orders, items = [d[x] for x in FILES]

    # 1. Data quality and dataset overview
    overview = []
    for name, df in d.items():
        overview.append({
            "table": name, "rows": len(df), "columns": len(df.columns),
            "duplicate_rows": int(df.duplicated().sum()),
            "missing_cells": int(df.isna().sum().sum())
        })
    save_table(pd.DataFrame(overview), "01_data_overview", out)

    # 2. Key integrity checks
    integrity = pd.DataFrame([
        ["events_customer_not_found", int((~events.customer_id.isin(customers.customer_id)).sum())],
        ["events_product_not_found", int((~events.product_id.isin(products.product_id)).sum())],
        ["orders_customer_not_found", int((~orders.customer_id.isin(customers.customer_id)).sum())],
        ["items_order_not_found", int((~items.order_id.isin(orders.order_id)).sum())],
        ["items_product_not_found", int((~items.product_id.isin(products.product_id)).sum())],
    ], columns=["check", "issue_count"])
    save_table(integrity, "02_integrity_checks", out)

    # 3. Funnel by distinct sessions
    funnel = (events.pivot_table(index="event_type", values="session_id", aggfunc="nunique")
              .reindex(["view_product", "add_to_cart", "begin_checkout", "purchase"])
              .fillna(0).rename(columns={"session_id": "unique_sessions"}).reset_index())
    funnel["conversion_from_product_views_pct"] = (
        funnel["unique_sessions"] / max(1, funnel.loc[0, "unique_sessions"]) * 100
    ).round(2)
    funnel["step_conversion_pct"] = (
        funnel["unique_sessions"] / funnel["unique_sessions"].shift(1) * 100
    ).round(2)
    save_table(funnel, "03_funnel_analysis", out)

    # 4. Cart and checkout abandonment, based on sessions
    session_steps = events.groupby("session_id").agg(
        viewed=("event_type", lambda x: (x == "view_product").any()),
        added=("event_type", lambda x: (x == "add_to_cart").any()),
        checkout=("event_type", lambda x: (x == "begin_checkout").any()),
        purchased=("event_type", lambda x: (x == "purchase").any()),
        customer_id=("customer_id", "first"),
        device_type=("device_type", "first"),
        traffic_source=("traffic_source", "first")
    ).reset_index()
    viewed_sessions = session_steps[session_steps.viewed]
    cart_sessions = session_steps[session_steps.added]
    checkout_sessions = session_steps[session_steps.checkout]
    cart_abandon = 1 - cart_sessions.purchased.mean() if len(cart_sessions) else np.nan
    checkout_abandon = 1 - checkout_sessions.purchased.mean() if len(checkout_sessions) else np.nan
    abandonment = pd.DataFrame([
        ["Cart abandonment rate", len(cart_sessions), int(cart_sessions.purchased.sum()), cart_abandon * 100],
        ["Checkout abandonment rate", len(checkout_sessions), int(checkout_sessions.purchased.sum()), checkout_abandon * 100],
    ], columns=["metric", "sessions_at_stage", "sessions_purchased", "rate_pct"])
    save_table(abandonment, "04_abandonment", out)

    # 5. Conversion by device and traffic source
    def group_conversion(col):
        return session_steps.groupby(col).agg(
            sessions=("session_id", "nunique"),
            product_view_sessions=("viewed", "sum"),
            cart_sessions=("added", "sum"),
            checkout_sessions=("checkout", "sum"),
            purchase_sessions=("purchased", "sum")
        ).reset_index().assign(
            session_to_purchase_pct=lambda x: (x.purchase_sessions / x.sessions * 100).round(2)
        )
    save_table(group_conversion("device_type"), "05_conversion_by_device", out)
    save_table(group_conversion("traffic_source"), "06_conversion_by_traffic_source", out)

    # 6. Product/category performance using events + order line items
    product_views = events[events.event_type == "view_product"].groupby("product_id").agg(
        views=("event_id", "count"), view_sessions=("session_id", "nunique")
    ).reset_index()
    product_carts = events[events.event_type == "add_to_cart"].groupby("product_id").agg(
        cart_adds=("event_id", "count"), cart_sessions=("session_id", "nunique")
    ).reset_index()
    item_sales = items.groupby("product_id").agg(
        units_sold=("quantity", "sum"), item_revenue_inr=("line_total_inr", "sum")
    ).reset_index()
    product_perf = products.merge(product_views, on="product_id", how="left").merge(
        product_carts, on="product_id", how="left").merge(item_sales, on="product_id", how="left")
    for c in ["views", "view_sessions", "cart_adds", "cart_sessions", "units_sold", "item_revenue_inr"]:
        product_perf[c] = product_perf[c].fillna(0)
    product_perf["view_to_cart_pct"] = np.where(product_perf.view_sessions > 0,
        product_perf.cart_sessions / product_perf.view_sessions * 100, 0).round(2)
    save_table(product_perf.sort_values("item_revenue_inr", ascending=False), "07_product_performance", out)

    category_perf = product_perf.groupby("category").agg(
        products=("product_id", "nunique"), views=("views", "sum"),
        cart_adds=("cart_adds", "sum"), units_sold=("units_sold", "sum"),
        item_revenue_inr=("item_revenue_inr", "sum")
    ).reset_index()
    category_perf["view_to_cart_pct"] = np.where(category_perf.views > 0,
        category_perf.cart_adds / category_perf.views * 100, 0).round(2)
    save_table(category_perf, "08_category_performance", out)

    # 7. Orders and customer metrics
    delivered = orders[orders.order_status == "Delivered"].copy()
    aov = delivered.total_amount_inr.mean() if len(delivered) else np.nan
    order_counts = orders.groupby("customer_id").agg(
        order_count=("order_id", "nunique"),
        total_spend_inr=("total_amount_inr", "sum"),
        average_order_value_inr=("total_amount_inr", "mean"),
        last_order_date=("order_date", "max")
    ).reset_index()
    order_counts["customer_type"] = np.where(order_counts.order_count > 1, "Repeat", "One-time")
    customer_metrics = customers.merge(order_counts, on="customer_id", how="left")
    customer_metrics[["order_count", "total_spend_inr", "average_order_value_inr"]] = (
        customer_metrics[["order_count", "total_spend_inr", "average_order_value_inr"]].fillna(0))
    customer_metrics["customer_type"] = customer_metrics["customer_type"].fillna("No order")
    save_table(customer_metrics, "09_customer_metrics", out)

    repeat_summary = customer_metrics.groupby("customer_type").agg(
        customers=("customer_id", "nunique"),
        revenue_inr=("total_spend_inr", "sum")
    ).reset_index()
    repeat_summary["customer_share_pct"] = (repeat_summary.customers / len(customers) * 100).round(2)
    save_table(repeat_summary, "10_customer_type_summary", out)

    # 8. Order status, payment, and monthly trends
    status_summary = orders.groupby("order_status").agg(
        orders=("order_id", "nunique"), order_value_inr=("total_amount_inr", "sum")
    ).reset_index()
    save_table(status_summary, "11_order_status_summary", out)
    payment_summary = orders.groupby("payment_method").agg(
        orders=("order_id", "nunique"), order_value_inr=("total_amount_inr", "sum")
    ).reset_index()
    save_table(payment_summary, "12_payment_summary", out)
    monthly = orders.dropna(subset=["order_date"]).assign(
        month=lambda x: x.order_date.dt.to_period("M").astype(str)
    ).groupby("month").agg(
        orders=("order_id", "nunique"), revenue_inr=("total_amount_inr", "sum"),
        customers=("customer_id", "nunique")
    ).reset_index()
    save_table(monthly, "13_monthly_orders", out)

    # 9. Basic RFM segmentation (recency relative to latest order in this dataset)
    if len(orders):
        reference_date = orders.order_date.max() + pd.Timedelta(days=1)
        rfm = orders.groupby("customer_id").agg(
            recency_days=("order_date", lambda x: (reference_date - x.max()).days),
            frequency=("order_id", "nunique"),
            monetary_inr=("total_amount_inr", "sum")
        ).reset_index()
        # Rank-based scores; duplicates are handled with percentile ranks.
        rfm["R_score"] = pd.qcut(rfm.recency_days.rank(method="first", ascending=False), 4, labels=[4,3,2,1]).astype(int)
        rfm["F_score"] = pd.qcut(rfm.frequency.rank(method="first"), 4, labels=[1,2,3,4]).astype(int)
        rfm["M_score"] = pd.qcut(rfm.monetary_inr.rank(method="first"), 4, labels=[1,2,3,4]).astype(int)
        rfm["RFM_score"] = rfm[["R_score","F_score","M_score"]].sum(axis=1)
        rfm["segment"] = np.select(
            [rfm.RFM_score >= 10, rfm.RFM_score >= 7, rfm.RFM_score >= 5],
            ["High value", "Potential loyalist", "Needs attention"], default="At risk")
        save_table(rfm, "14_rfm_segments", out)

    # 10. Charts (matplotlib defaults; no fixed colour palette)
    plt.figure(figsize=(8,5))
    plt.bar(funnel.event_type, funnel.unique_sessions)
    plt.title("E-commerce Shopping Funnel")
    plt.ylabel("Unique sessions")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(out / "funnel.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8,5))
    cat_plot = category_perf.sort_values("item_revenue_inr", ascending=False)
    plt.bar(cat_plot.category, cat_plot.item_revenue_inr)
    plt.title("Revenue by Product Category")
    plt.ylabel("Item revenue (INR)")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(out / "category_revenue.png", dpi=160)
    plt.close()

    # 11. Executive KPI snapshot
    kpis = pd.DataFrame([
        ["Total customers", len(customers)],
        ["Total products", len(products)],
        ["Total sessions", events.session_id.nunique()],
        ["Total orders", orders.order_id.nunique()],
        ["Delivered-order AOV (INR)", round(aov,2) if pd.notna(aov) else None],
        ["Session-to-purchase conversion (%)", round(session_steps.purchased.mean()*100,2)],
        ["Cart abandonment (%)", round(cart_abandon*100,2) if pd.notna(cart_abandon) else None],
        ["Checkout abandonment (%)", round(checkout_abandon*100,2) if pd.notna(checkout_abandon) else None],
    ], columns=["KPI","value"])
    save_table(kpis, "00_executive_kpis", out)

    print(f"Analysis complete. Outputs saved to: {out.resolve()}")
    print(kpis.to_string(index=False))

if __name__ == "__main__":
    main()
