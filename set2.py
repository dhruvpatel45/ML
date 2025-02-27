import pandas as pd
import matplotlib.pyplot as plt

#1 Load the dataset
df = pd.read_csv('cars_data.csv') 
print("Last 5 records:")
print(df.tail())

# 2 Print the size and shape of the DataFrame
print("\nSize of the DataFrame:", df.size)
print("Shape of the DataFrame:", df.shape)

#3 Find the mean price for each brand
mean_price_per_brand = df.groupby('Brand')['Price'].mean()
print("\nMean price for each brand:")
print(mean_price_per_brand)

# 4 Count the cars having Black color
black_cars_count = df[df['Color'] == 'Black'].shape[0]
print("\nCount of cars having Black color:", black_cars_count)

# 5 Find which Brand has the maximum cars in the year 2017
max_cars_2017 = df[df['Year'] == 2017]['Brand'].value_counts().idxmax()
print("\nBrand with maximum cars in the year 2017:", max_cars_2017)

# 6 Create a line chart showing the proportion for each car brand
brand_counts = df['Brand'].value_counts()
brand_counts.plot(kind='line', marker='o')
plt.title('Proportion of Each Car Brand')
plt.xlabel('Car Brand')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# 7 Print the statistical information of the DataFrame
print("\nStatistical information of the DataFrame:")
print(df.describe())

# 8 Remove all duplicate values from the DataFrame
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)

# 9 Count the null values in the DataFrame and replace with median value
null_counts = df.isnull().sum()
print("\nCount of null values in each column:")
print(null_counts)

# Replace null values with median
df.fillna(df.median(), inplace=True)
print("\nDataFrame after replacing null values with median:")
print(df)