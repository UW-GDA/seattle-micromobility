#!/usr/bin/env python
"""This file is used to fetch new gtfs data regularly."""
import os
from pathlib import Path
import json
from datetime import datetime
from gbfs.services import SystemDiscoveryService


OUTPUT_DIR = os.path.join(Path(__file__).parent.parent, 'raw_data')
LIME_SEATTLE = 'lime_seattle'
FEED_NAME = 'free_bike_status'


def run():
    ds = SystemDiscoveryService()
    client = ds.instantiate_client(LIME_SEATTLE)

    time_of_system_query = datetime.now()
    system_status = client.request_feed(FEED_NAME)

    output_filename = f"bikeshare_system_status_{time_of_system_query.strftime('%Y-%m-%d_%H-%M-%S')}.json"
    output_filepath = os.path.join(OUTPUT_DIR, output_filename)

    with open(output_filepath, "w") as output_file:
        json.dump(system_status["data"]["bikes"], output_file)


if __name__ == "__main__":
    run()