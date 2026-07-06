import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('data/processed/cleaned_online_retail.csv')

engine = create_engine('postgresql+psycopg2://postgres:<PASSWORD>@localhost:5432/ecommerce')

df.to_sql("clean_retail", engine, if_exists="replace", index=False)

print("Data loaded successfully into PostgreSQL database.")