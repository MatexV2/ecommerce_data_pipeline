import pandas as pd
file_path = 'Data/Raw/Online_Retail.csv'

df = pd.read_csv(file_path)

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


