# Module: eda.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_entry_exit_times(metadata):
    metadata['hour'] = metadata['timestamp'].dt.hour
    sns.histplot(metadata['hour'], bins=24, kde=False)
    plt.title('Vehicle Entry/Exit Times')
    plt.xlabel('Hour of Day')
    plt.ylabel('Frequency')
    plt.show()

def plot_parking_occupancy(entry_data, exit_data):
    entry_data['date'] = entry_data['timestamp'].dt.date
    exit_data['date'] = exit_data['timestamp'].dt.date

    entry_counts = entry_data.groupby('date').size()
    exit_counts = exit_data.groupby('date').size()
    occupancy = entry_counts - exit_counts

    occupancy.plot(kind='bar')
    plt.title('Parking Occupancy by Day')
    plt.xlabel('Date')
    plt.ylabel('Number of Vehicles')
    plt.show()

# Usage
entry_data = pd.read_csv(entry_dataset_path)
exit_data = pd.read_csv(exit_dataset_path)
entry_data['timestamp'] = pd.to_datetime(entry_data['timestamp'])
exit_data['timestamp'] = pd.to_datetime(exit_data['timestamp'])

plot_entry_exit_times(metadata)
plot_parking_occupancy(entry_data, exit_data)
