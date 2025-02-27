import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('movies.csv')


#1. Load data set using pandas function and print top 10 record.
print("Top 10 Records:")
print(df.head(10))

#2. Which movie earns the most and least profit?
df['Profit'] = df['revenue'] - df['budget']
most_profitable = df.loc[df['Profit'].idxmax()]
least_profitable = df.loc[df['Profit'].idxmin()]
print("Most Profitable Movie:", most_profitable['title'], "with profit of", most_profitable['Profit'])
print("Least Profitable Movie:", least_profitable['title'], "with profit of", least_profitable['Profit'])

#3. Print movies which have a value of '0' in their budget or revenue.
zero_budget_revenue = df[(df['budget'] == 0) | (df['revenue'] == 0)]
print("Movies with 0 budget or revenue:")
print(zero_budget_revenue[['title', 'budget', 'revenue']])

#4.  Calculate the total Profits made by all movies in  year which it released.
yearly_profit = df.groupby('release_year')['Profit'].sum()
print("Total profits by year:")
print(yearly_profit)

#5.  Draw line chart for run time of movie. 
plt.figure(figsize=(10, 5))
plt.plot(df['runtime'], marker='o', linestyle='-', color='b')
plt.xlabel('Movie Index')
plt.ylabel('Runtime (minutes)')
plt.title('Movie Runtimes')
plt.show()

#6. In which year we had the most movies making profits?
profitable_movies = df[df['Profit'] > 0]
year_most_profitable_movies = profitable_movies['release_year'].value_counts().idxmax()
print("Year with most profitable movies:", year_most_profitable_movies)

#7  Print the size and shape of the data set.
print("Dataset Size:", df.size)
print("Dataset Shape:", df.shape)

#8. Remove the duplicate  record from the dataset
df.drop_duplicates(inplace=True)
print("Duplicates removed. New shape:", df.shape)

#9. Count the null values in the data set and fill with the average value.
print("Null Values:")
print(df.isnull().sum())
df.fillna(df.mean(numeric_only=True), inplace=True)
print("Null values replaced with column average.")
