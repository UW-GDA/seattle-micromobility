from datetime import datetime


def extract_timestamp(filename: str) -> datetime:
    # Extract the date and time portion from the filename
    # example filename: blah_blah_blah_2025-02-19_00-00-00.json
    parts = filename.split('_')
    date_part = parts[-2]  # Extract YYYY-MM-DD
    time_part = parts[-1].split('.')[0]  # Extract HH-MM-SS
    timestamp_str = date_part + "_" + time_part
    return datetime.strptime(timestamp_str, "%Y-%m-%d_%H-%M-%S")