# E-Commerce Product Analytics & Customer Behaviour Analysis

An end-to-end data analytics project focused on understanding customer purchasing behaviour, analysing product performance, evaluating the e-commerce conversion funnel, and identifying opportunities to improve business performance.

The project uses Python, SQL, and Power BI-oriented DAX measures to transform raw e-commerce data into actionable business insights.

---

## Project Overview

This project analyses a fictional fashion and lifestyle e-commerce platform using a synthetic dataset containing over **114,000 records** across customers, products, website events, orders, and order items.

The objective is to understand how customers interact with an e-commerce platform, identify factors influencing purchase decisions, evaluate shopping cart abandonment, and measure product and category performance.

The project follows an end-to-end analytics workflow, from data preparation and exploratory analysis to SQL-based business queries and dashboard-oriented KPI development.

## Business Objectives

- Analyse customer purchasing patterns and shopping behaviour.
- Evaluate the customer journey from product discovery to purchase.
- Identify conversion gaps and cart abandonment trends.
- Compare product and category-level performance.
- Understand customer retention and repeat purchasing behaviour.
- Analyse order value, payment methods, and order statuses.
- Develop actionable recommendations for improving the shopping experience.

## Tools & Technologies

| Tool | Application |
|---|---|
| Python | Data cleaning, analysis and visualisation |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualisation |
| MySQL | Database management and business queries |
| Power BI | Dashboard development and KPI reporting |
| DAX | Business metrics and calculated measures |
| VS Code | Development environment |
| GitHub | Project documentation and version control |

## Dataset Description

The project uses a synthetic India-focused e-commerce dataset with 5 interconnected CSV files.

| Dataset | Records | Description |
|---|---:|---|
| Customers | 10,000 | Customer demographics and information |
| Products | 1,000 | Product catalogue and attributes |
| Events | 94,913 | Customer browsing and shopping interactions |
| Orders | 3,662 | Order-level transaction information |
| Order Items | 5,039 | Individual products included in orders |
| **Total** | **114,614** | **Combined records** |

The dataset includes customer activity such as product views, add-to-cart events, checkout initiation, and purchases.

**Data disclaimer:** All records are synthetically generated for educational and portfolio purposes. They are not actual Myntra data or confidential business information.

## Key Performance Indicators (KPIs)

The initial Python analysis generated the following executive metrics:

| KPI | Result |
|---|---:|
| Total Customers | 10,000 |
| Total Products | 1,000 |
| Total Sessions | 30,000 |
| Total Orders | 3,662 |
| Delivered-Order AOV | ₹2,791.48 |
| Session-to-Purchase Conversion | 12.21% |
| Cart Abandonment | 64.52% |
| Checkout Abandonment | 38.85% |

## Analysis Performed

### 1. Customer Behaviour Analysis
- Customer activity and purchasing patterns.
- New versus repeat customer analysis.
- Customer-level spending metrics.
- RFM-based customer segmentation.

### 2. Product & Category Analysis
- Product-level performance evaluation.
- Category-wise revenue analysis.
- Identification of product performance trends.

### 3. E-Commerce Conversion Funnel
- Product views.
- Add-to-cart interactions.
- Checkout initiation.
- Purchase completion.
- Cart and checkout abandonment analysis.

### 4. Order & Revenue Analysis
- Average Order Value (AOV).
- Monthly order trends.
- Payment method distribution.
- Delivered, cancelled and returned order analysis.

### 5. Customer Acquisition Analysis
- Conversion by device.
- Conversion by traffic source.
- Comparison of customer engagement and purchasing behaviour.

## Key Business Observations

The initial analysis highlights several opportunities for further investigation:

- Cart abandonment of 64.52% indicates considerable scope to improve the shopping journey.
- Checkout abandonment of 38.85% suggests potential friction during the final purchase stages.
- Session-to-purchase conversion of 12.21% provides a baseline for evaluating conversion performance.
- Customer segmentation can help identify high-value customers and opportunities for retention.
- Product and category performance analysis can support better merchandising and promotional decisions.

## Project Structure

```text
ecommerce-product-analytics/
│
├── ecommerce_product_analytics_dataset/
│   ├── customers.csv
│   ├── products.csv
│   ├── events.csv
│   ├── orders.csv
│   └── order_items.csv
│
├── ecommerce_product_analytics_all_codes/
│   ├── python/
│   │   └── analyse_ecommerce.py
│   ├── sql/
│   │   ├── 01_schema.sql
│   │   └── 02_analysis_queries.sql
│   ├── power_bi/
│   │   └── 03_dax_measures.txt
│   ├── requirements.txt
│   └── README_CODES.md
│
├── outputs/
│   ├── 00_executive_kpis.csv
│   ├── 01_data_overview.csv
│   ├── 02_integrity_checks.csv
│   ├── 03_funnel_analysis.csv
│   ├── 04_abandonment.csv
│   ├── 05_conversion_by_device.csv
│   ├── 06_conversion_by_traffic_source.csv
│   ├── 07_product_performance.csv
│   ├── 08_category_performance.csv
│   ├── 09_customer_metrics.csv
│   ├── 10_customer_type_summary.csv
│   ├── 11_order_status_summary.csv
│   ├── 12_payment_summary.csv
│   ├── 13_monthly_orders.csv
│   ├── 14_rfm_segments.csv
│   ├── category_revenue.png
│   └── funnel.png
│
└── README.md
```

## How to Run the Project

### Python Analysis

1. Install Python.
2. Install the required libraries:

```bash
pip install pandas numpy matplotlib
```

3. Run the analysis script from the main project directory:

```bash
py ecommerce_product_analytics_all_codes/python/analyse_ecommerce.py --data-dir ecommerce_product_analytics_dataset
```

4. The generated reports and visualisations will be saved in the `outputs` folder.

### SQL Analysis

- Import the five CSV datasets into MySQL.
- Execute `01_schema.sql` to create the database tables.
- Run `02_analysis_queries.sql` to perform business analysis.

### Power BI

- Import the generated CSV reports or connect to the prepared MySQL database.
- Establish the appropriate table relationships.
- Use the provided DAX measures to build KPI cards, conversion funnel visuals, customer analysis, and product performance dashboards.

## Future Enhancements

- Develop an interactive Power BI dashboard.
- Build a Tableau dashboard for comparative business reporting.
- Perform deeper customer cohort and retention analysis.
- Develop product recommendation strategies.
- Explore predictive modelling for customer purchase behaviour.
- Identify opportunities for improving conversion and customer lifetime value.

## Project Outcome

This project demonstrates the application of data analytics to e-commerce business problems, combining data processing, customer behaviour analysis, SQL querying, KPI development, and business-oriented interpretation.

It bridges technical analytics with product and business decision-making by translating customer and transaction data into measurable performance indicators and potential improvement opportunities.

---

**Project Category:** Data Analytics | E-Commerce | Product Analytics | Customer Behaviour Analysis

**Disclaimer:** This is an independent portfolio project using synthetic data. It is not affiliated with or endorsed by Myntra or any other e-commerce company.
