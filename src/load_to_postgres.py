import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

database_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    database=os.environ["DB_NAME"],
)

df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "cleaned_online_retail.csv"
)

engine = create_engine(database_url)

df.to_sql(
    "clean_retail", engine, if_exists="replace", index=False
)

print("Data loaded successfully into PostgreSQL database.")