from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "data" / "raw" / "online_retail.csv"

df = pd.read_csv(file_path, encoding="latin1")

print(df.head())
print(df.info())
print(df.describe())
print(df.isna().sum());

print("\nNegative quantities:")
print((df["Quantity"] < 0).sum())

print("\nNegative prices:")
print((df["UnitPrice"] < 0).sum())

print("\nUnique customers:")
print(df["CustomerID"].nunique())

print("\nUnique invoices:")
print(df["InvoiceNo"].nunique())

print("\nCountries:")
print(df["Country"].nunique())


