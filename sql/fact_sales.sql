create table fact_sales as
select
    "StockCode" as product_id,
    "CustomerID" as customer_id,
    "InvoiceNo" as invoice_id,
    "InvoiceDate" as invoice_date,
    "Quantity" as quantity,
    "UnitPrice" as unit_price,
    ("Quantity" * "UnitPrice")::numeric as revenue
from "clean_retail";
