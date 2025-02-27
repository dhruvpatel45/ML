import pandas as pd
import matplotlib.pyplot as plt

#1 Load the dataset
df = pd.read_csv('diamonds.csv')
print("Last 5 records:")
print(df.tail())

#2 Draw the bar chart of costliest and cheapest diamonds
costliest_diamond = df.loc[df['price'].idxmax()]
cheapest_diamond = df.loc[df['price'].idxmin()]

# Create a DataFrame for plotting
costs = pd.DataFrame({
    'Diamond': ['Costliest', 'Cheapest'],
    'Price': [costliest_diamond['price'], cheapest_diamond['price']]
})

plt.figure(figsize=(8, 5))
plt.bar(costs['Diamond'], costs['Price'], color=['gold', 'silver'])
plt.title('Costliest and Cheapest Diamonds')
plt.ylabel('Price')
plt.show()

#3 Draw the chart for Price vs Carat of Diamonds
plt.figure(figsize=(10, 6))
plt.scatter(df['carat'], df['price'], alpha=0.5)
plt.title('Price vs Carat of Diamonds')
plt.xlabel('Carat')
plt.ylabel('Price')
plt.grid()
plt.show()

#4 Print the record where either of dimension (x, y, z) is zero
zero_dimensions = df[(df['x'] == 0) | (df['y'] == 0) | (df['z'] == 0)]
print("\nRecords where either of dimension (x, y, z) is zero:")
print(zero_dimensions)

#5 Create a new DataFrame by multiplying x, y, z
df['volume'] = df['x'] * df['y'] * df['z']
print("\nDataFrame with volume (x * y * z) added:")
print(df[['x', 'y', 'z', 'volume']].head())

#6 Drop all the dimensions (x, y, z)
df_dropped = df.drop(columns=['x', 'y', 'z'])
print("\nDataFrame after dropping dimensions (x, y, z):")
print(df_dropped.head())

#7 Print all the statistical information of the DataFrame
print("\nStatistical information of the DataFrame:")
print(df.describe())

#8 Remove all the duplicate values from the DataFrame
df_no_duplicates = df_dropped.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)

#9 Count the null values in the DataFrame and replace with mean value
null_counts = df_no_duplicates.isnull().sum()
print("\nCount of null values in each column:")
print(null_counts)

# Replace null values with mean
df_no_duplicates.fillna(df_no_duplicates.mean(), inplace=True)
print("\nDataFrame after replacing null values with mean:")
print(df_no_duplicates)