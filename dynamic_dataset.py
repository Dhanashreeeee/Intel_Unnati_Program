import pandas as pd

def initialize_dynamic_datasets(entry_dataset_path, exit_dataset_path):
    columns = ['timestamp', 'plate_number']
    entry_df = pd.DataFrame(columns=columns)
    exit_df = pd.DataFrame(columns=columns)
    
    entry_df.to_csv(entry_dataset_path, index=False)
    exit_df.to_csv(exit_dataset_path, index=False)

def update_dynamic_datasets(plate_number, entry_dataset_path, exit_dataset_path, action='entry'):
    dataset_path = entry_dataset_path if action == 'entry' else exit_dataset_path
    df = pd.read_csv(dataset_path)
    
    new_record = {'timestamp': datetime.now(), 'plate_number': plate_number}
    df = df.append(new_record, ignore_index=True)
    df.to_csv(dataset_path, index=False)

# Usage
entry_dataset_path = "entry_dataset.csv"
exit_dataset_path = "exit_dataset.csv"
initialize_dynamic_datasets(entry_dataset_path, exit_dataset_path)
