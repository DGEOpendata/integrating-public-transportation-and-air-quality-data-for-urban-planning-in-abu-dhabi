python
import pandas as pd

# Load datasets
transport_data = pd.read_csv('public_transport_usage_2020.csv')
air_quality_data = pd.read_csv('air_quality_index_2020.csv')

# Merge datasets on a common column (e.g., date)
merged_data = pd.merge(transport_data, air_quality_data, on='date')

# Example analysis: Correlation between ridership and air quality
correlation = merged_data[['ridership', 'PM2.5']].corr()

print("Correlation between ridership and PM2.5 levels:")
print(correlation)

# Visualize the data
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(merged_data['date'], merged_data['ridership'], label='Ridership')
plt.plot(merged_data['date'], merged_data['PM2.5'], label='PM2.5 Levels')
plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Public Transport Ridership vs Air Quality')
plt.legend()
plt.show()
