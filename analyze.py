# analyze.py
# 1. DataFrame ingestion - Read local clean_games.json into a Pandas DataFrame
# 2. Metadata inspection - Print the total number of records that made it through cleaning system
# 3. Statistical Aggregation: Calculate and print the mean Metacritic score of games list
# 4. Data Slicing - identify and print the single highest-rated game in the dataset

import pandas as pd

# ingest local JSON file into DataFrame
df = pd.read_json("clean_games.json")

# Display structural details about the DataFrame columns and data types
print(df.info())

# count the total rows in these specific columns
total_rows = len(df)

# compute the mean (average) of the specified column's values
column_average = df["metacritic"].mean()

# finds the index location of the highest value in 'metacritic'
highest_value_index = df["metacritic"].idxmax()

# Extracts the entire row matching that specific index location
top_record_row = df.loc[highest_value_index]

# Accesses a specific value from that matching row
top_record_name = top_record_row["name"]

print(f"Total Processing Records: {total_rows}")
print(f"Calculated System Average: {column_average:.2f}")
print(top_record_name)
