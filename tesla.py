import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:\Users\kirthick\Downloads\archive\TSLA.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Sort data
df = df.sort_values(by='Date')

# Show first rows
print(df.head())

# Basic info
print(df.info())

# Check missing values
print(df.isnull().sum())

# Create new column (Daily Change)
df['Daily Change'] = df['Close'] - df['Open']

# Summary statistics
print(df.describe())

# 📊 Plot Closing Price
plt.figure()
plt.plot(df['Date'], df['Close'])
plt.title("Tesla Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.xticks(rotation=45)
plt.show()

# 📊 Plot Volume
plt.figure()
plt.plot(df['Date'], df['Volume'])
plt.title("Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.xticks(rotation=45)
plt.show()

# Save cleaned data
df.to_csv("cleaned_tsla.csv", index=False)