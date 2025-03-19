# Seattle Micromobility Scripts

## Getting Started

We created several scripts to help in the data cleaning and processing steps for our analysis.
We will describe the intended usage for each script.
Their possible configurations and current limitations will be outlined.

### 1. Gathering Bikeshare System Data using [`bikeshare-client-python`](https://github.com/jakehadar/bikeshare-client-python)

#### Script: `scripts/fetch_gbfs_data.py`

This script uses the `bikeshare-client-python` created by [Jake Hadar](https://github.com/jakehadar) to connect to the Lime Bikeshare Feed.
The bikeshare data feed is maintained in accordance with the General Bikeshare Feed Specification ([GBFS](https://github.com/MobilityData/gbfs?tab=readme-ov-file#what-is-gbfs)) which allows us to use this library to query it.

#### What does it do?

1. Define Constants
    * filepath location to save the results of the bikeshare system query
    * the system of interest, in our case this is `lime_seattle` and
    * the feed name which is an option within a specific system client see docs for [`bikeshare-client-python`](https://github.com/jakehadar/bikeshare-client-python) or the [GBFS](https://github.com/MobilityData/gbfs?tab=readme-ov-file#what-is-gbfs) documentaion for more information.
2. Connect to and instantiate Bikeshare system client
3. Request feed and save to a `.json` file.

#### How do I run it?
`./scripts/fetch_gbfs_data.py`

#### Notes and Limitations
Before running this script be sure to alter any of the constants to match the bikeshare system of your interest.
We are not guaranteeing that the filepathing is robust for any system.
This is a known potential source of issues.


### 2. Refining GBFS Data Queried from Bikeshare System

#### Script: `scripts/refine_raw_data_time_samples.py`

This script is more of a hacky solution to a problem we faced which you may not ever need.
Our goal was to run the querying script every 30 minutes for a week or so to gather the bikshare system status data we needed.
It turned out getting the script to run every 30 minutes on a personal macbook air was troublesome.
A slightly different variation of the previous script was run on a teammates lab computer which accidentally ran several times during each 30th minute (a small bug).
This resulted in excessive datasamples on our 30 minute interval, therefore, this script was created to subsample down to just one snapshot of the bikeshare system every 30 minutes.

#### What does it do?

1. Subsamples the snapshots of the bikeshare system down to one query file every 30 minutes by
    * Creates a list of files to keep
    * Copies the files in the list over to a desired directory

#### How do I run it?
`./scripts/refine_raw_data_time_samples.py`

#### Notes and Limitations
Only configuration here is 1) where are the files starting, 2) where are the files going to be copied to, and 3) how many minutes apart should the files be subsampled down to (defaults to 30).
Note, these are not parameters of the script but are rather hard coded at the moment.
Perhaps in the future with more time we will come back and expand this script, but it is not a hight priority since it was the hacky solution to a larger issue that we would rather solve first.

### 3. Process Raw GBFS Data

#### Script: `scripts/process_raw_gbfs.py`

This query reads in all of the `.json` files from the bikeshare system queries (output from the `fetch_gbfs_data.py`) and saves a compiled and tidied up version to a `.geojson` using [GeoPandas](https://geopandas.org/en/stable/index.html).

#### What does it do?

1. Define Constants
    * filepath location of the outputs from the `scripts/fetch_gbfs_data.py` script
    * filepath location to save the results of the bikeshare system query
2. For each bikeshare system status `.json` file
    * Load the contents into a pandas DataFrame
    * Add a datetime column based on when the system status query took place
    * Create geometries from the bikeshare system status `lat` and `lon` data
    * Create a GeoPandas GeoDataFrame
3. Concatenate all of the GeoPandas GeoDataFrames together
4. Save the collective GeoDataFrame to a `.geojson` file in the desired output directory.

#### How do I run it?
`./scripts/process_raw_gbfs.py`

#### Notes and Limitations
Be sure to verify that the filename formatting in this script is the same as when you ran `scripts/fetch_gbfs_data.py`.
Additionally, there is furtherwork to be done with respect to running this more often over specific batchs of the bikeshare query data.
For example, this could be extended to take as an input a new set of system query `.json` files which are ready to be processed.
As it stands today, rerunning this script would produce bloating data redundency in that it would always create a new `.geojson` gradually getting larger since it includes all the previous data again and any new data that has been collected since last running.
In it's current state it is not intended to be run over and over, without great care and a few changes to extend it's configurabilities.

### 4. Animate Bikeshare System Evolution Over Time

#### Script: `scripts/process_raw_gbfs.py`

This script can create animations of how the bikeshare system status evolves over time for all of Seattle or for a particular neighborhood.

<p float="left">
  <img src="../visuals/bike_share_system_evolution_Downtown_2025-02-22_2025-02-22.gif" width="250" />
  <img src="../visuals/bike_share_system_evolution_University_District_2025-02-22_2025-02-22.gif" width="250" />
  <img src="../visuals/bike_share_system_evolution_Seattle_2025-02-22_2025-02-22.gif" width="250" />
</p>

**Important Note** this script is extremely coupled to and dependant on the data being visualized being from Seattle.
It is possible to extend this to another city or location, but would require extra work including locating easy to access `geojson` files for the city of interest (city limits and nieghborhood boundaries).

#### Prerequisites
You should have generated a `geojson` file with the bikeshare system statuses using both the `/scripts/fetch_gbfs_data.py` and `scripts/process_raw_gbfs.py` scripts.

#### What does it do?

1. Load the Bikeshare System Status GeoDataFrame created with the `scripts/process_raw_gbfs.py` script.
2. Load Seattle City boundary GeoDataFrame
3. Load Seattle Neighborhood boundary GeoDataFrame (then dissolve the minor neighborhoods into the larger more common ones)
4. filter the bikeshare GeoDataFrame on the start date plus number of days and the neighborhood
5. Create animation using `matplotlib`

#### How do I run it?
`./scripts/process_raw_gbfs.py` (implicitly relying on default values) or alternatively use the configurable parameters.

#### What are my configuration options?
`--bikeshare_file` the file which contains the bikeshare system status geojson from `scripts/process_raw_gbfs.py`.

`--date` the date for which to start the bikeshare system status evolution animation, must be within the window of data in the `--bikeshare_file`.

`--num_days` the number of days of data to animate in the bikeshare system evolution, be mindful that a longer window of time will take longer to animate. **Warning** It has note been tested with more than one day.

`--neighborhood` an eligable neighborhood in Seattle (or the area of interest if you have extended this beyond the Seattle use case), worst case scenario there is an issue with spelling of the nieghborhood or it's just not in our dataset and the error message will display all eligible neighborhoods.

#### Notes and Limitations

Many have been highlighted already, but it is good to call out again, this is extremely tied to Seattle.
It would not be offal to extend to a more general setting, but would take some careful work.