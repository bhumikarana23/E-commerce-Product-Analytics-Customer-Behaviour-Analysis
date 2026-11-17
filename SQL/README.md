# SQL – E-Commerce Business & Customer Analytics

## Overview

This folder contains the SQL scripts developed for the **E-Commerce Product Analytics & Customer Behaviour Analysis** project.

The SQL component focuses on database creation, relational data management, analytical querying, and extracting business insights from e-commerce customer, product, browsing, and transaction data.

MySQL is used to organise the datasets into relational tables and perform structured business analysis.

## Tools & Technologies

- MySQL
- MySQL Workbench
- SQL
- Relational Database Management

## SQL Files

| File | Description |
|---|---|
| `01_schema.sql` | Creates the database, tables, primary keys, foreign keys, and indexes |
| `02_analysis_queries.sql` | Contains SQL queries for business and customer analytics |

## Database Structure

The database consists of five interconnected tables:

| Table | Description |
|---|---|
| customers | Customer information and signup details |
| products | Product catalogue and attributes |
| events | Customer browsing and shopping interactions |
| orders | Order-level transaction information |
| order_items | Individual products associated with orders |

### Table Relationships

- `customer_id` connects customers with their events and orders.
- `product_id` connects products with browsing events and order items.
- `order_id` connects orders with their corresponding order items.

These relationships enable integrated analysis across customer activity, product performance, and purchasing behaviour.

## SQL Analysis Performed

### 1. Database Management
- Database and table creation.
- Primary and foreign key constraints.
- Index creation.
- Relational database organisation.

### 2. Customer Analytics
- Total customer analysis.
- New versus repeat customer analysis.
- Customer purchase frequency.
- Customer spending behaviour.
- Customer-level performance metrics.

### 3. Product Analytics
- Product-level sales performance.
- Category-wise revenue analysis.
- Top-performing products.
- Product demand evaluation.

### 4. Sales & Revenue Analytics
- Total orders and sales analysis.
- Average Order Value (AOV).
- Monthly order trends.
- Payment method distribution.
- Order status analysis.
- Discount and transaction analysis.

### 5. Conversion Funnel Analytics
- Product view analysis.
- Add-to-cart activity.
- Checkout initiation.
- Purchase completion.
- Session-to-purchase conversion.
- Cart and checkout abandonment.

### 6. Acquisition & Retention Analytics
- Device-wise conversion analysis.
- Traffic source performance.
- Repeat purchase behaviour.
- Customer retention opportunities.

## Business Questions Addressed

The SQL analysis is designed to investigate questions such as:

1. How many customers and products are present in the database?
2. Which product categories generate the highest revenue?
3. Which products perform best in terms of sales?
4. What proportion of shopping carts result in purchases?
5. Which devices generate better purchase conversion?
6. Which traffic sources contribute to customer purchases?
7. What is the average delivered-order value?
8. How does order volume change over time?
9. What percentage of customers make repeat purchases?
10. Which customers contribute the most revenue?
11. What are the most common order statuses?
12. Which payment methods are most frequently used?

## How to Execute

### Step 1: Open MySQL Workbench

Connect to your MySQL server.

### Step 2: Create the Database

Open and execute:

`01_schema.sql`

This creates the database and its relational table structure.

### Step 3: Import the Datasets

Import the five CSV datasets into their corresponding database tables.

Ensure that column names and data types match the schema.

### Step 4: Execute Analysis Queries

Open:

`02_analysis_queries.sql`

Execute the queries individually or section by section to generate analytical results.

## Project Objective

The SQL component demonstrates the application of relational database management and analytical querying to practical e-commerce business problems.

It complements the Python analysis and supports the development of business intelligence dashboards using Power BI.

## Disclaimer

The database uses entirely synthetic data generated for educational, analytical, and portfolio development purposes.

It does not contain actual customer records, transactions, or proprietary data from Myntra or any other e-commerce company.

---

**Project:** E-Commerce Product Analytics & Customer Behaviour Analysis

**Folder:** SQL

**Database:** MySQL

**Purpose:** Database Management, Business Analytics & Data Exploration
