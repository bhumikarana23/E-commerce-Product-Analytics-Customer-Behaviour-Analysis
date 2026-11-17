# Python – E-Commerce Data Analysis

## Overview

This folder contains the Python implementation of the **E-Commerce Product Analytics & Customer Behaviour Analysis** project.

The analysis script uses Python to process and analyse e-commerce datasets, generate business performance metrics, examine customer purchasing behaviour, and create visualisations.

The implementation focuses on transforming structured customer, product, event, and transaction data into meaningful analytical outputs.

## Python Script

### `analyse_ecommerce.py`

The main Python script performs end-to-end data analysis using the five interconnected datasets:

- Customers
- Products
- Events
- Orders
- Order Items

## Libraries Used

| Library | Purpose |
|---|---|
| Pandas | Data loading, cleaning, manipulation and analysis |
| NumPy | Numerical calculations and data operations |
| Matplotlib | Charts and data visualisation |

## Analysis Performed

### 1. Data Overview & Integrity
- Dataset size and structure analysis.
- Record and column overview.
- Data integrity checks.

### 2. Customer Behaviour Analysis
- Customer-level metrics.
- New and repeat customer summaries.
- RFM-based customer segmentation.

### 3. E-Commerce Funnel Analysis
- Product views.
- Add-to-cart activities.
- Checkout initiation.
- Purchase completion.
- Conversion and abandonment calculations.

### 4. Product Performance Analysis
- Product-level performance.
- Category-wise revenue analysis.
- Product performance comparisons.

### 5. Sales & Order Analysis
- Average Order Value (AOV).
- Monthly order trends.
- Payment method analysis.
- Order status distribution.

### 6. Acquisition & Conversion Analysis
- Conversion by device.
- Conversion by traffic source.
- Customer session and purchase behaviour.

## Key Performance Indicators

The script generates executive-level KPIs, including:

- Total customers.
- Total products.
- Total sessions.
- Total orders.
- Delivered-order Average Order Value.
- Session-to-purchase conversion rate.
- Cart abandonment rate.
- Checkout abandonment rate.

## Generated Outputs

After successful execution, the script creates an `outputs` folder containing analytical reports and visualisations.

| Output File | Description |
|---|---|
| 00_executive_kpis.csv | Executive-level business KPIs |
| 01_data_overview.csv | Dataset overview |
| 02_integrity_checks.csv | Data integrity results |
| 03_funnel_analysis.csv | Conversion funnel metrics |
| 04_abandonment.csv | Cart and checkout abandonment |
| 05_conversion_by_device.csv | Device-wise conversion |
| 06_conversion_by_traffic_source.csv | Traffic source analysis |
| 07_product_performance.csv | Product-level performance |
| 08_category_performance.csv | Category-level performance |
| 09_customer_metrics.csv | Customer-level metrics |
| 10_customer_type_summary.csv | New versus repeat customers |
| 11_order_status_summary.csv | Order status analysis |
| 12_payment_summary.csv | Payment method analysis |
| 13_monthly_orders.csv | Monthly order trends |
| 14_rfm_segments.csv | RFM customer segmentation |
| category_revenue.png | Category revenue visualisation |
| funnel.png | E-commerce conversion funnel chart |

## Installation & Execution

### Step 1: Install Required Libraries

```bash
pip install pandas numpy matplotlib
```

### Step 2: Execute the Analysis Script

Run the following command from the main project directory:

```bash
py ecommerce_product_analytics_all_codes/python/analyse_ecommerce.py --data-dir ecommerce_product_analytics_dataset
```

### Step 3: Access Generated Results

After execution, the generated CSV reports and PNG visualisations will be available in the `outputs` folder.

## Tools & Environment

- Programming Language: Python
- Development Environment: Visual Studio Code
- Data Analysis: Pandas, NumPy
- Visualisation: Matplotlib
- Input Format: CSV
- Output Formats: CSV and PNG

## Project Objective

The Python component demonstrates practical data analytics capabilities through data processing, exploratory analysis, customer segmentation, conversion funnel evaluation, KPI calculation, and business-oriented visualisation.

It forms the analytical foundation for the broader SQL and Power BI components of the project.

---

**Project:** E-Commerce Product Analytics & Customer Behaviour Analysis

**Folder:** Python

**Primary Script:** `analyse_ecommerce.py`

**Purpose:** Data Analysis & Business Intelligence
