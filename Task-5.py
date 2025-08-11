import pandas as pd
import matplotlib.pyplot as plt
import io
# Creating a dummy CSV data in-memory to simulate loading from a file
csv_data = """Date,Product,Sales,Region
2023-01-01,A,150,North
2023-01-01,B,200,South
2023-01-02,A,160,North
2023-01-02,C,100,East
2023-01-03,B,250,South
2023-01-03,A,170,West
2023-01-04,C,120,East
2023-01-04,B,300,West
2023-01-05,A,180,North
2023-01-05,C,110,East
"""
# 1. Load CSV using Pandas
df = pd.read_csv(io.StringIO(csv_data))
print("Original DataFrame:")
print(df.head())
print("\n" + "="*30 + "\n")
# 2. Group by 'Product' and calculate the sum of 'Sales'
product_sales = df.groupby('Product')['Sales'].sum().reset_index()
print("Total Sales by Product:")
print(product_sales)
print("\n" + "="*30 + "\n")
# 3. Group by 'Region' and calculate the sum of 'Sales'
region_sales = df.groupby('Region')['Sales'].sum().reset_index()
print("Total Sales by Region:")
print(region_sales)
print("\n" + "="*30 + "\n")
# 4. Plotting the data
plt.figure(figsize=(12, 5))
# Plot 1: Total Sales by Product
plt.subplot(1, 2, 1)
plt.bar(product_sales['Product'], product_sales['Sales'], color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
# Plot 2: Total Sales by Region
plt.subplot(1, 2, 2)
plt.pie(region_sales['Sales'], labels=region_sales['Region'], autopct='%1.1f%%', startangle=90, colors=['coral', 'lightgreen', 'gold', 'skyblue'])
plt.title('Sales Distribution by Region')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()