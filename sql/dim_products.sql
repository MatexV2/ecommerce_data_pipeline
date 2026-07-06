create table dim_products as
select
    "StockCode" as product_id,
    min("Description") as product_name
from "clean_retail"
group by(product_id);
