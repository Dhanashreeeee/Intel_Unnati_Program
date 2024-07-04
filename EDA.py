# Module: eda.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_entry_exit_times(metadata):
    metadata['vehicle_timestamp'] = pd.to_datetime(metadata['vehicle_timestamp'])
    metadata['hour'] = metadata['vehicle_timestamp'].dt.hour
    sns.histplot(metadata['hour'], bins=24, kde=False)
    plt.title('Vehicle Entry/Exit Times')
    plt.xlabel('Hour of Day')
    plt.ylabel('Frequency')
    plt.show()

def plot_parking_occupancy(metadata):
    metadata['date'] = metadata['vehicle_timestamp'].dt.date
    occupancy = metadata.groupby('date').size()
    occupancy.plot(kind='bar')
    plt.title('Parking Occupancy by Day')
    plt.xlabel('Date')
    plt.ylabel('Number of Vehicles')
    plt.show()

# Usage
plot_entry_exit_times(metadata)
plot_parking_occupancy(metadata)
