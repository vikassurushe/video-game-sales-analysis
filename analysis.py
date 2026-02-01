import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))
csv_path = os.path.join(DATA_DIR, "vgsales.csv")

df = pd.read_csv(csv_path)

# Graph 1: Top 10 Games by Global Sales
top10_games = df.sort_values("Global_Sales", ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.barh(top10_games["Name"], top10_games["Global_Sales"])
plt.xlabel("Global Sales (Millions)")
plt.ylabel("Game Name")
plt.title("Top 10 Games by Global Sales")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Graph 2: Platform-wise Global Sales
platform_sales = (
    df.groupby("Platform")["Global_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 5))
platform_sales.plot(kind="bar")
plt.xlabel("Platform")
plt.ylabel("Total Global Sales (Millions)")
plt.title("Top 10 Platforms by Global Sales")
plt.tight_layout()
plt.show()

# Graph 3: Year-wise Global Sales Trend
year_sales = df.groupby("Year")["Global_Sales"].sum().sort_index()

plt.figure(figsize=(10, 5))
plt.plot(year_sales.index, year_sales.values)
plt.xlabel("Year")
plt.ylabel("Global Sales (Millions)")
plt.title("Year-wise Global Sales Trend")
plt.tight_layout()
plt.show()
