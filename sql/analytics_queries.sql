-- 1. Total Revenue

select
    round(sum(revenue), 2) as total_revenue
from fact_sales;

-- 2. Revenue by Customer

select
    customer_id,
    round(sum(revenue), 2) as revenue
from fact_sales
group by customer_id
order by revenue desc;

-- 3. Monthly Revenue Trend

select
    date_trunc('month', invoice_date::timestamp) as month,
    round(sum(revenue), 2) as revenue
from fact_sales
group by month
order by month;

-- 4. Top 10 Customers by Revenue

select
    customer_id,
    round(sum(revenue), 2) as revenue
from fact_sales
group by customer_id
order by revenue desc
limit 10;

-- 5. Number of Orders per Customer

select
    customer_id,
    count(distinct invoice_id) as orders_count
from fact_sales
group by customer_id
order by orders_count desc;

-- 6. Average Order Value (AOV)

select
    round(avg(order_value), 2) as average_order_value
from (
    select
        invoice_id,
        sum(revenue) as order_value
    from fact_sales
    group by invoice_id
) order_values;

-- 7. Top 10 Products by Quantity Sold

select
    product_id,
    sum(quantity) as units_sold
from fact_sales
group by product_id
order by units_sold desc
limit 10;

-- 8. Customer Metrics

select
    customer_id,
    count(distinct invoice_id) as total_orders,
    round(sum(revenue), 2) as total_revenue
from fact_sales
group by customer_id
order by total_revenue desc;

-- 9. Monthly Number of Orders

select
    date_trunc('month', invoice_date::timestamp) as month,
    count(distinct invoice_id) as orders
from fact_sales
group by month
order by month;

-- 10. Revenue per Invoice

select
    invoice_id,
    round(sum(revenue), 2) as invoice_value
from fact_sales
group by invoice_id
order by invoice_value desc
limit 10;