create table dim_customers as
select 
    "CustomerID" as customer_id,
    min("Country") as customer_country
from "clean_retail"
group by customer_id;
