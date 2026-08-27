import pandas as pd
import matplotlib.pyplot as plt

# 1. Create Data
data = {
    'OrderID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Laptop', 'Monitor', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [60000, 800, 60000, 2000, 800, 62000, 15000, 800, 2000, 15000],
    'Quantity': [1, 2, 1, 1, 3, 1, 2, 2, 1, 1],
    'City': ['Bangalore', 'Bangalore', 'Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Mumbai', 'Bangalore', 'Bangalore'],
    'OrderDate': pd.to_datetime(['2024-01-15', '2024-01-20', '2024-02-10', '2024-02-15', '2024-03-05', '2024-03-18', '2024-03-20', '2024-04-02', '2024-04-10', '2024-04-15'])
}
df = pd.DataFrame(data)
df['TotalSales'] = df['Price'] * df['Quantity']
df['Month'] = df['OrderDate'].dt.month_name()

print("--- E-COMMERCE SALES ANALYSIS PROJECT ---\n")
print(df)

# 2. Analysis
print("\n--- Sales by Product ---")
print(df.groupby('Product')['TotalSales'].sum())

print("\n--- Sales by City ---")
print(df.groupby('City')['TotalSales'].sum())

# 3. Graphs - This will make your project stand out
plt.figure(figsize=(8,4))
df.groupby('Product')['TotalSales'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.ylabel('Sales in Rs')
plt.show()

plt.figure(figsize=(8,4))
df.groupby('City')['TotalSales'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales by City')
plt.ylabel('')
plt.show()

print("\nProject Complete!")