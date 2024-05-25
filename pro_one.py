import pandas as pd

file_path = "D:\my\python\main.csv" 
df = pd.read_csv(file_path)
categories = df["category"].unique()
category_data = {}
for category in categories:
    category_df = df[df["category"] == category]
    category_data[category] = category_df

for category, data in category_data.items():
    output_file = f"{category}_cleaned.csv" 
    data.to_csv(output_file, index=False)
    print(f"Data for '{category}' category has been cleaned and saved to '{output_file}'.")

print("All data has been cleaned and saved successfully.")
