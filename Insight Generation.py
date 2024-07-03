import pandas as pd
import matplotlib.pyplot as plt

def generate_insights(metadata):
    vehicle_times = metadata['vehicle_timestamp']
    vehicle_times = pd.to_datetime(vehicle_times)
    
    # Movement Patterns
    plt.figure(figsize=(10, 6))
    sns.histplot(vehicle_times, bins=24, kde=True)
    plt.title('Vehicle Movement Patterns')
    plt.xlabel('Time of Day')
    plt.ylabel('Number of Vehicles')
    plt.show()

    # Parking Occupancy
    occupancy = vehicle_times.dt.hour.value_counts().sort_index()
    
    plt.figure(figsize=(10, 6))
    occupancy.plot(kind='bar')
    plt.title('Parking Occupancy by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Vehicles')
    plt.show()

# Usage
data_dir = "realtime_vehicle_data"
metadata = load_metadata(data_dir)
generate_insights(metadata)
