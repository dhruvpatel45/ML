import pandas as pd

#1 Load the dataset
df = pd.read_csv('flights_data.csv')  
print("Last 5 records:")
print(df.tail())

#2 Print the number of flights from one point to another
flight_counts = df.groupby(['Origin', 'Destination']).size().reset_index(name='Number of Flights')
print("\nNumber of flights from one point to another:")
print(flight_counts)

#3 Find the best airline in terms of departure
best_airline = df.loc[df['DepartureDelay'].idxmin(), 'Airline']
print("\nBest airline in terms of departure (minimum delay):", best_airline)

#4 Create a new column 'Speed' by calculating speed of airplane using distance and time taken to travel
df['Speed'] = df['Distance'] / df['FlightTime']  # Speed = Distance / Time
print("\nDataFrame with Speed column added:")
print(df[['Distance', 'FlightTime', 'Speed']].head())

#5 Create a DataFrame containing the total number of flights going to a particular destination
destination_counts = df['Destination'].value_counts().reset_index()
destination_counts.columns = ['Destination', 'Total Flights']
print("\nTotal number of flights going to each destination:")
print(destination_counts)

#6 Find the size and shape of the dataset
print("\nShape of the DataFrame:", df.shape)
print("Size of the DataFrame:", df.size)

#7 Print all the column headers of the DataFrame
print("\nColumn headers of the DataFrame:")
print(df.columns.tolist())

#8 Remove all duplicate values from the DataFrame
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)

#9 Count the null values in the DataFrame and replace with mean value
null_counts = df.isnull().sum()
print("\nCount of null values in each column:")
print(null_counts)

# Replace null values with mean
df.fillna(df.mean(), inplace=True)
print("\nDataFrame after replacing null values with mean:")
print(df)