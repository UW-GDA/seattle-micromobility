import os
import shutil
from datetime import timedelta
from common.helpers import extract_timestamp


def select_files(directory: str) -> list[str]:
    files = []
    
    for filename in os.listdir(directory):
        timestamp = extract_timestamp(filename)
        if timestamp:
            files.append((timestamp, filename))
    
    # Sort files by timestamp
    files.sort()
    
    selected_files = []
    last_selected_time = None
    
    for timestamp, filename in files:
        if last_selected_time is None or (timestamp - last_selected_time) >= timedelta(minutes=30):
            selected_files.append(filename)
            last_selected_time = timestamp
    
    return selected_files


def copy_files(file_list: str, source_directory: str, destination_directory: str) -> None:
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    for filename in file_list:
        source_path = os.path.join(source_directory, filename)
        destination_path = os.path.join(destination_directory, filename)
        shutil.copy2(source_path, destination_path)


def subset_of_raw_data(input_dir: str, output_dir: str) -> None:
    selected = select_files("raw_data_from_bo/")
    copy_files(selected, input_dir, output_dir)

    return "Success"


if __name__ == "__main__":
    result = subset_of_raw_data("raw_data_from_bo/", "raw_data/")
    print(result)
    selected = select_files("raw_data/")
    # print(*selected, sep='\n')
    print("Count", len(selected))
