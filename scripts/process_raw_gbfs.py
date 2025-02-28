import os
from datetime import datetime
import geopandas as gpd
import pandas as pd

from common.helpers import extract_timestamp

RAW_GBFS_DATA_DIR = "raw_data/"
PROCESSED_GBFS_DATA_DIR = "processed_gbfs_data/"

bikeshare_gdf_prev = None

if __name__ == "__main__":
    for filename in os.listdir(RAW_GBFS_DATA_DIR):
        print(f"Processing {filename}")
        try:
            time_of_system_query = extract_timestamp(filename)

            string_ts = time_of_system_query.strftime("%Y-%m-%d_%H-%M-%S")

            filename = os.path.join(RAW_GBFS_DATA_DIR, f"bikeshare_system_status_{string_ts}.json")

            bikeshare_df = pd.read_json(filename)
            bikeshare_df["datetime"] = time_of_system_query

            geometry = gpd.points_from_xy(bikeshare_df.lon, bikeshare_df.lat)
            bikeshare_gdf = gpd.GeoDataFrame(bikeshare_df, geometry=geometry)
            bikeshare_gdf.set_crs("EPSG:4326", inplace=True)
            bikeshare_gdf.to_crs("EPSG:32610", inplace=True)

            bikeshare_gdf_prev = pd.concat([bikeshare_gdf, bikeshare_gdf_prev], ignore_index=True)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    output = os.path.join(PROCESSED_GBFS_DATA_DIR, f"bikeshare_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.geojson")
    bikeshare_gdf_prev.to_file(output, driver="GeoJSON")