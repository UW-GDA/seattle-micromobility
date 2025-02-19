import requests
import json

OUTPUT_FILE = "data/station_information.json"

def get_gbfs_data(url):
    """Fetches and parses GBFS data from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return None

def main():
    """Main function to demonstrate GBFS data access."""
    # gbfs_url = "https://data.lime.bike/api/partners/v1/gbfs/seattle/gbfs.json" # Replace with the actual GBFS URL
    # gbfs_url = "https://data.lime.bike/api/partners/v1/gbfs/seattle/system_information.json" # Replace with the actual GBFS URL
    # gbfs_url = "https://data.lime.bike/api/partners/v1/gbfs/seattle/station_information.json" # Replace with the actual GBFS URL
    # gbfs_url = "https://data.lime.bike/api/partners/v1/gbfs/seattle/station_status.json" # Replace with the actual GBFS URL
    gbfs_url = "https://data.lime.bike/api/partners/v1/gbfs/seattle/free_bike_status.json" # Replace with the actual GBFS URL
    gbfs_data = get_gbfs_data(gbfs_url)

    if gbfs_data:
        print("GBFS Data:")
        print(json.dumps(gbfs_data, indent=2)) # Print formatted JSON
        
        #Accessing specific data:
        try:
            station_info_url = next(feed["url"] for feed in gbfs_data["data"]["en"]["feeds"] if feed["name"] == "station_information")
            station_info = get_gbfs_data(station_info_url)
            if station_info:
              print("\nStation Information:")
              with open(OUTPUT_FILE, 'w') as json_file:
                json.dumps(station_info, json_file, indent=2)
        except (KeyError, StopIteration) as e:
            print(f"Error accessing data: {e}")

if __name__ == "__main__":
    main()
