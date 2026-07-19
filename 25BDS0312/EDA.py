import pandas as pd
df = pd.read_csv("C:/Users/desai/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/LocalState/sessions/F61FE62CF77B2CC03BC87F3252361ECF470FA9FE/transfers/2026-29/1000 Sales Records.csv")

print("=" * 60)
print("1. FIRST 5 ROWS")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("2. LAST 5 ROWS")
print("=" * 60)
print(df.tail())

print("\n" + "=" * 60)
print("3. DATASET INFORMATION")
print("=" * 60)
df.info()

print("\n" + "=" * 60)
print("4. STATISTICAL SUMMARY")
print("=" * 60)
print(df.describe())

print("\n" + "=" * 60)
print("5. COUNT OF RECORDS IN EACH REGION")
print("=" * 60)
print(df["Region"].value_counts())

print("\n" + "=" * 60)
print("6. AVERAGE TOTAL PROFIT BY REGION")
print("=" * 60)
average_profit = df.groupby("Region")["Total Profit"].mean()
print(average_profit)

print("\n" + "=" * 60)
print("7. TOP 5 RECORDS SORTED BY UNITS SOLD")
print("=" * 60)
sorted_data = df.sort_values(by="Units Sold", ascending=False)
print(sorted_data.head())

print("\n" + "=" * 60)
print("8. MISSING VALUES IN EACH COLUMN")
print("=" * 60)
print(df.isnull().sum())

print("\n" + "=" * 60)
print("9. ONLINE SALES RECORDS (FIRST 5)")
print("=" * 60)
online_sales = df[df["Sales Channel"] == "Online"]
print(online_sales.head())

print("\n" + "=" * 60)
print("10. ADDING A NEW COLUMN: PROFIT MARGIN")
print("=" * 60)
df["Profit Margin"] = df["Total Profit"] / df["Total Revenue"]
print(df[["Country", "Total Revenue", "Total Profit", "Profit Margin"]].head())


