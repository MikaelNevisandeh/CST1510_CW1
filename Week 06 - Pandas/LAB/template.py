import pandas as pd

# 1. Read the CSV file into a DataFrame from the LAB folder
df = pd.read_csv("LAB/security_data.csv")

# 2. Add the percent column calculated from your data
df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

# 3. Print the resulting DataFrame to the screen
print(df)
