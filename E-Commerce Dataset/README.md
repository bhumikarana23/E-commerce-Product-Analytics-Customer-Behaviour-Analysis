# E-Commerce Product Analytics – Dataset Documentation

## Overview

This folder contains the synthetic dataset developed for the **E-Commerce Product Analytics & Customer Behaviour Analysis** project.

The dataset represents a fictional India-focused fashion and lifestyle e-commerce platform and is designed to simulate customer interactions, product browsing activities, purchasing behaviour, and order transactions.

It contains **114,614 records across five interconnected CSV files**, providing a foundation for exploratory data analysis, customer segmentation, product performance evaluation, conversion funnel analysis, and business intelligence reporting.

## Dataset Summary

| Dataset | Records | Description |
|---|---:|---|
| customers.csv | 10,000 | Customer information and signup details |
| products.csv | 1,000 | Product catalogue and attributes |
| events.csv | 94,913 | Customer browsing and shopping activities |
| orders.csv | 3,662 | Order-level transaction records |
| order_items.csv | 5,039 | Individual products within customer orders |
| **Total** | **114,614** | **Combined records** |

## File Descriptions

### 1. customers.csv
Contains customer-level information used to analyse customer demographics, acquisition, and purchasing behaviour.

### 2. products.csv
Contains product catalogue information used for product-level and category-level performance analysis.

### 3. events.csv
Records customer interactions with the e-commerce platform, including:

- Product views
- Add-to-cart activities
- Checkout initiation
- Purchase events

This dataset supports customer journey and conversion funnel analysis.

### 4. orders.csv
Contains order-level information used to evaluate transaction performance, order values, payment methods, and order statuses.

### 5. order_items.csv
Contains individual product entries associated with orders, enabling detailed basket-level and product sales analysis.

## Dataset Relationships

The five datasets are interconnected through common identifiers:

- `customer_id` connects customers with their events and orders.
- `product_id` connects products with browsing events and order items.
- `order_id` connects orders with their corresponding order items.

The relationships allow customer-level, product-level, and transaction-level analysis across the dataset.

**Note:** The `product_id` recorded in a purchase event represents the primary product associated with that event. For complete order basket analysis, use `order_items.csv`.

## Dataset Characteristics

- **Geographical focus:** India
- **Currency:** Indian Rupee (INR)
- **Data format:** CSV
- **Event period:** 2025
- **Customer signup period:** 2024–2025
- **Platform type:** Fictional fashion and lifestyle e-commerce platform
- **Data type:** Synthetic / Artificially Generated

## Potential Applications

This dataset can be used for:

1. Exploratory Data Analysis (EDA)
2. Customer behaviour and purchasing pattern analysis
3. E-commerce conversion funnel analysis
4. Shopping cart and checkout abandonment analysis
5. Product and category performance evaluation
6. Customer segmentation using RFM analysis
7. Revenue and order trend analysis
8. SQL-based business intelligence queries
9. Power BI dashboard development
10. Customer retention and repeat purchase analysis

## Tools Used

- Python
- Pandas
- NumPy
- MySQL
- Power BI
- DAX
- Matplotlib

## Important Disclaimer

This dataset is entirely synthetic and was generated for educational, analytical, and portfolio development purposes.

It does not contain actual customer information, real transactions, or proprietary business data from Myntra or any other e-commerce company.

The dataset is intended to simulate realistic e-commerce scenarios and demonstrate practical data analytics workflows.

---

**Project:** E-Commerce Product Analytics & Customer Behaviour Analysis

**Dataset Size:** 114,614 records

**Format:** Five CSV files

**Purpose:** Academic learning, portfolio development, and business analytics practice.
