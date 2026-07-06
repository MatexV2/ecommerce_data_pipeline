import pandas as pd

df = pd.read_csv("data/raw/online_retail.csv", encoding="latin1")

print("Before cleaning:", df.shape)

df = df[df["CustomerID"].notna()]
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

df = df.copy()

df["CustomerID"] = df["CustomerID"].astype(int)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("After cleaning:", df.shape)

print("Missing values:")
print(df.isnull().sum())

print("\nData summary:")
print(df.describe())

df.to_csv("data/processed/cleaned_online_retail.csv", index=False)

print("File saved.")