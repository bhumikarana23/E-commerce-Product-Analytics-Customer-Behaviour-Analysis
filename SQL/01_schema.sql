-- MySQL 8.0+ schema for the synthetic e-commerce dataset.
CREATE DATABASE IF NOT EXISTS ecommerce_analytics;
USE ecommerce_analytics;

CREATE TABLE customers (
  customer_id VARCHAR(20) PRIMARY KEY,
  signup_date DATE,
  age_group VARCHAR(10),
  gender VARCHAR(30),
  city VARCHAR(60),
  state VARCHAR(60),
  loyalty_tier VARCHAR(20),
  marketing_opt_in BOOLEAN
);

CREATE TABLE products (
  product_id VARCHAR(20) PRIMARY KEY,
  product_name VARCHAR(150),
  category VARCHAR(40),
  subcategory VARCHAR(60),
  brand VARCHAR(60),
  gender_segment VARCHAR(20),
  list_price_inr INT,
  discount_percent INT,
  rating DECIMAL(2,1),
  review_count INT,
  inventory_status VARCHAR(30),
  selling_price_inr INT
);

CREATE TABLE orders (
  order_id VARCHAR(20) PRIMARY KEY,
  customer_id VARCHAR(20),
  session_id VARCHAR(20),
  order_date DATE,
  subtotal_inr DECIMAL(12,2),
  discount_inr DECIMAL(12,2),
  shipping_fee_inr DECIMAL(12,2),
  total_amount_inr DECIMAL(12,2),
  payment_method VARCHAR(20),
  order_status VARCHAR(20),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  order_item_id VARCHAR(20) PRIMARY KEY,
  order_id VARCHAR(20),
  product_id VARCHAR(20),
  quantity INT,
  unit_price_inr DECIMAL(12,2),
  line_total_inr DECIMAL(12,2),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE events (
  event_id VARCHAR(20) PRIMARY KEY,
  session_id VARCHAR(20),
  customer_id VARCHAR(20),
  event_timestamp DATETIME,
  product_id VARCHAR(20),
  event_type VARCHAR(30),
  device_type VARCHAR(30),
  traffic_source VARCHAR(40),
  order_id VARCHAR(20),
  campaign_id VARCHAR(40),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE INDEX idx_events_session ON events(session_id);
CREATE INDEX idx_events_type ON events(event_type);
CREATE INDEX idx_events_timestamp ON events(event_timestamp);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_date ON orders(order_date);
