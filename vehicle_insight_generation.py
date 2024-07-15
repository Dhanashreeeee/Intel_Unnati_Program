# Module: insight_generation.py
import pandas as pd

def generate_insights(entry_data, exit_data):
    entry_data['hour'] = entry_data['timestamp'].dt.hour
    exit_data['hour'] = exit_data['timestamp'].dt.hour
    
    peak_entry_time = entry_data['hour'].value_counts().idxmax()
    peak_exit_time = exit_data['hour'].value_counts().idxmax()
    
    print(f"Peak Entry Time: {peak_entry_time}:00 - {peak_entry_time + 1}:00")
    print(f"Peak Exit Time: {peak_exit_time}:00 - {peak_exit_time + 1}:00")

    entry_data['date'] = entry_data['timestamp'].dt.date
    exit_data['date'] = exit_data['timestamp'].dt.date

    entry_counts = entry_data.groupby('date').size()
    exit_counts = exit_data.groupby('date').size()
    occupancy = entry_counts - exit_counts
    
    print("Average Parking Occupancy by Day:")
    print(occupancy.mean())

# Usage
generate_insights(entry_data, exit_data)
