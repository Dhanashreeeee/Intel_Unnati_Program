import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_vehicle_entry_exit_times(metadata):
    vehicle_times = metadata['vehicle_timestamp']
    vehicle_times = pd.to_datetime(vehicle_times)
    
    plt.figure(figsize=(10, 6))
    sns.histplot(vehicle_times, bins=24, kde=True)
    plt.title('Vehicle Entry and Exit Times')
    plt.xlabel('Time of Day')
    plt.ylabel('Number of Vehicles')
    plt.show()

def plot_parking_occupancy(metadata):
    vehicle_times = metadata['vehicle_timestamp']
    vehicle_times = pd.to_datetime(vehicle_times)
    
    occupancy = vehicle_times.dt.hour.value_counts().sort_index()
    
    plt.figure(figsize=(10, 6))
    occupancy.plot(kind='bar')
    plt.title('Average Parking Occupancy by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Vehicles')
    plt.show()

# Usage
data_dir = "realtime_vehicle_data"
metadata = load_metadata(data_dir)
plot_vehicle_entry_exit_times(metadata)
plot_parking_occupancy(metadata)
