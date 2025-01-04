import pandas as pd

# Load the dataset
data = pd.read_excel('data/sales_data.xlsx')

# Clean and preprocess data
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.to_period('M')
data_grouped = data.groupby(['Month', 'Product'])['Sales'].sum().reset_index()

# Save the cleaned data
data_grouped.to_csv('output/cleaned_sales_data.csv', index=False)
print("Data cleaned and saved successfully.")
