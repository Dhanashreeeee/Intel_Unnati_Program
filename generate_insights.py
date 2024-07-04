# Module: generate_insights.py
def generate_insights(metadata):
    # Example insights
    vehicle_entry_exit_times = metadata[['vehicle_image_path', 'vehicle_timestamp']]
    avg_parking_occupancy = metadata['vehicle_timestamp'].dt.hour.value_counts().mean()
    
    insights = {
        "Vehicle Entry and Exit Times": vehicle_entry_exit_times,
        "Average Parking Occupancy": avg_parking_occupancy
    }
    
    return insights

# Usage
insights = generate_insights(metadata)
for key, value in insights.items():
    print(f"{key}:\n{value}\n")
