import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
data = pd.read_csv('output/cleaned_sales_data.csv')

# Create a line plot for monthly sales trends
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Month', y='Sales', hue='Product', marker='o')
plt.title('Monthly Sales Trends by Product')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output/sales_trends.png')
plt.show()
