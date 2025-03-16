import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite database
connection = sqlite3.connect('amazon_scraper.db')

# Load the data into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM products", connection)

# Close the database connection
connection.close()

# Display the first few rows of the DataFrame
print(df.head())

# Data Analysis and Visualization

# Convert price to numeric (remove commas and convert to float)
df['price'] = df['price'].str.replace(',', '').astype(float)

# Histogram of product prices
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=20, kde=True)
plt.title('Distribution of Product Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Bar chart of product availability
availability_counts = df['availability'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=availability_counts.index, y=availability_counts.values)
plt.title('Product Availability')
plt.xlabel('Availability')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Scatter plot of price vs. reviews
df['reviews'] = df['reviews'].str.replace(',', '').str.extract('(\d+)').astype(float)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['reviews'], y=df['price'])
plt.title('Price vs. Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('Price')
plt.show()