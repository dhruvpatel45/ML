import pandas as pd
import matplotlib.pyplot as plt

# 1 Load the dataset
df = pd.read_csv('iris.csv')  
print("First 4 records:")
print(df.head(4))

# 2 Print information of the dataset
print("\nInformation of the dataset:")
print(df.info())

# 3 Count the values of each class of species
species_counts = df['species'].value_counts()
print("\nCount of each class of species:")
print(species_counts)

# 4 Draw a line chart for sepal-length vs sepal-width
plt.figure(figsize=(10, 6))
plt.plot(df['sepal_length'], df['sepal_width'], 'o-')
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.grid()
plt.show()

# 5 Print shape and size of the DataFrame
print("\nShape of the DataFrame:", df.shape)
print("Size of the DataFrame:", df.size)

# 6 Print all the column headers of the DataFrame
print("\nColumn headers of the DataFrame:")
print(df.columns.tolist())

# 7 Filter the records from index no 80 to 100
filtered_records = df.iloc[80:101]  # iloc is inclusive of the start and exclusive of the end
print("\nRecords from index 80 to 100:")
print(filtered_records)

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