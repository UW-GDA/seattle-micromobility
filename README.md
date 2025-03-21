# **Seattle Micromobility: Spatiotemporal Analysis, Safety Hotspots & Geographic Influences** 🚲🛴

**Group members:** Abdul-Razak Alidu, Sruangsaeng Chaikasetsin, Hunter Lybbert, Ysabel Yu

---
## Table of Contents

1. [Summary](#1-summary)
2. [Introductory Background](#2-introductory-background)
3. [Problem Statement & Objectives](#3-problem-statement--objectives)
4. [Datasets](#4-datasets)
5. [Tools & Packages](#5-tools--packages)
6. [Methodology & Approach](#6-methodology--approach)
7. [Results, Conclusions, and Future Directions](#7-results-conclusions-and-future-directions)
8. [References](#8-references)

---
 
## 1. Summary
This project investigates **micromobility usage**-specifically e-scooters and bike share in Seattle. Our primary focus is to understand **where** and **when** people ride, locate potential **collision hotspots** involving vulnerable road users (pedestrians, cyclists, e-scooter riders), and examine **geographic factors** (like slope, transit proximity, land use) that may influence both usage and collisions. We hope these insights will guide data-driven enhancements to infrastructure, user behavior, and environmental considerations- ultimately fostering safer and more sustainable micromobility adoption.

### Contents of the repo:
* [**notebooks**](notebooks/) contains our jupyter notebooks where a majority of the data analysis we performed took place.
There are subdirectories for each aspect of the work: [bikeshare](notebooks/bikeshare/) analysis, [collision](notebooks/collision/) analysis, and [raster](notebooks/raster/) based analysis
* [**visuals**](visuals/) contains the many visualizations that we have created for this project.
* [**sample_data**](sample_data/) contains a collection of samples of the data we used.
Not all of the data could be included due to size constraints.
* [**scripts**](scripts/) contains the scripts used in gathering and processing the bikeshare data.

---

## 2. Introductory Background

Seattle has rapidly expanded its micromobility offerings (e-scooters, bike shares) to provide **low-emission**, last-mile travel solutions. For example, **Seattle's e-scooter pilot program** recorded over **1.4 millions rides** between 2020 and 2021 (Seattle Department of Transportation (SDOT), 2021). Meanwhile, a **2022 study by the National Association of City Transportation Officials (NACTO)** found that micromobility devices can replace up to **30% of short car trips** in dense urban areas, emphasizing their role in reducing vehicle miles traveled (NACTO, 2022). However, questions about **safety** and **usage distribution** persist. According to **SDOT collision data**, **21% of reported e-scooter crashes** in 2021 led to serious injuries-indicating the need for improved infrastructure and rider education (SDOT, 2022). Additionally, **steep slopes**, **uneven access to protected lanes**, and **transit deserts** may further complicate safe micromobility usage for residents in certain neighborhoods (King County Mobility Coalition, 2020)
By merging **trip data** (where and when people ride) with **collision records** and relevant **geospatial layers** (slope, transit stops, land-use types), we aim to

- Pinpoint **high-usage corridors** and **collision hotspots**
- Explore **geographic influences** (e.g., terrain, neighborhood zoning) on ridership and collisions

---

## 3. Problem Statement & Objectives

**Problem Statement**
1. **Where** do e-scooter and bike share trips cluster, and do these align with collision-prone zones?
2. **How** do factors like slope, proximity to infracstructure, or land use affect micromobility usage and crash risk?

**Objectives**
1. **Spatiotemporal Patterns**
    - Identify ridership peaks (daily/weekly/seasonal) and produce usage hotspot maps.
2. **Collision Hotspots**
    - Detect VRU collision clusters using Kernel Density Estimation (KDE) to compare with usage patterns.
3. **Geographic Factors**
    - Integrate slope or land-use data to see how terrain/environment shapes micromobility usage and collisions.

---

## 4. Datasets
1. **Micromobility Trip Data** 🚲🛴  
**General Bikeshare Feed Specification (GBFS)** – Standardized format for bike/scooter share data  
🔗 [GitHub Repository](https://github.com/MobilityData/gbfs)  
    - **Bird Feed**  
    - **Lime Feed**
2. **Seattle Micromobility & Collision Data** 🏙️  
    **Seattle Open GIS Portal**  
🔗 [Seattle GIS Open Data](https://data-seattlecitygis.opendata.arcgis.com)  
    - **🚦 Collision Data**  
        - Seattle SDOT Collisions (All Years)  
    - **🚲 Infrastructure & Facilities**  
        - SDOT Bike Facilities  
        - Bicycle Racks  
        - Sidewalks  
    - **Seattle Open Data Portal**  

3. **Geographic & Slope Data** 🌍  
    - **🔗 [Washington State DNR LiDAR Portal](https://lidarportal.dnr.wa.gov/#45.85941:-120.23438:6)** – 2016 King Country high-resolution LiDAR elevation data for slope analysis  

---

## 5. Tools & Packages

* Tools/packages used
    * [Geopandas](https://github.com/geopandas/geopandas)
    * [Numpy](https://github.com/numpy/numpy)
    * [Matplotlib](https://github.com/matplotlib/matplotlib)
    * [Rasterio](https://github.com/rasterio/rasterio)
    * [Rioxarray](https://github.com/corteva/rioxarray)
    * [Xarray](https://github.com/pydata/xarray)
    * [Rasterstats](https://github.com/perrygeo/python-rasterstats)
    * [Contextily](https://github.com/geopandas/contextily)
    * [bikeshare-client-python](https://github.com/jakehadar/bikeshare-client-python) to access ([GBFS](https://gbfs.org/guide/))
---

## 6. Methodology & Approach

**Spatiotemporal Patterns**: Bikeshare counter data was plotted on maps by Seattle neighborhood and turned into animations to show bikeshare changes over time. Scooter and bike distribbutions were plotted using Kernel Density Estimation to find micromobility use hotspots. This data was also used to do a time series analysis per hour and per day to find patterns in usage.

**Collision Hotspots**: For our collision hotspot analysis, we examined Seattle Department of Transportation (SDOT) collision data from 2020 to February 2025, focusing on crashes involving vulnerable road users (VRUs) such as pedestrians, cyclists, and scooter riders. We began by cleaning the dataset—removing duplicates, addressing missing values, converting date-time fields for consistency, and setting the appropriate coordinate reference system (CRS) for geospatial work. Next, we conducted exploratory analysis to tally collisions by year and assess severity, finding that 21% resulted in serious injuries. To uncover spatiotemporal patterns, we mapped crashes by hour, day, and month, then applied Kernel Density Estimation (KDE) to identify hotspot locations. We also performed a proximity analysis using GeoPandas’ `sjoin_nearest` function to determine how many collisions occurred within 50 meters of bike facilities and sidewalks, revealing infrastructure-related risks. Finally, we calculated per-capita collision rates by neighborhood, normalizing crash counts per 1000 residents to highlight areas with disproportionate risk. This multi-step approach, detailed in `notebooks/collision`, anchors our safety insights. 

**Geospatial Correlation**:
Geospatial correlation methods were split into 2 main parts: raster manipulation and road zonal stats. Firstly, a full Seattle DTM raster was created from smaller raster sets provided by King County. From this a slope raster was created and used to calculate zonal stats for roads in U District and Downtown. The stats showed the mean slope of those roads and highlighted where slopes were greatest using plots.

## 7. Results, Conclusions, and Future Directions

**Conclusion**

Our analysis revealed key safety insights for Seattle’s micromobility landscape. 
- **Micromobility Usage**:  High-usage zones like Downtown and U District often correlate with more crashes
- **Safety Gaps**: High-usage zones like Downtown often correlate with more crashes, but infrastructure plays a critical role—bike facilities show higher risks (~60% of collisions) compared to multi-used trails (~5%), likely due to conflict with the vehicle traffic.
- **Geographic Factor**: Slope is not an indicator for any of the above.
- **Limits**: A key limitation is that collision data lacks real-time trip counts, making usage overlap estimates approximate rather than precise.

**Future Directions**

To build on this work, we propose several next steps:
- **Normalize collision rates** with actual trip data (not just availability) for a clearer usage-crash link.
- **Expand land use analysis** to include factors like transit stops and commercial zones, which may further influence risk.
- **Refine hotspot detection** using DBSCAN to identify tighter, more actionable clusters compared to KDE’s broader smoothing.


## 8. References
1. Seattle Department of Transportation (SDOT).** (2021). *E-Scooter Pilot Program Evaluation Report. Seattle, WA.
2. National Association of City Transportation Officials (NACTO). (2022). Shared Micromobility in the U.S.: 2022 Snapshot. [https://nacto.org](https://nacto.org)
3. Seattle Department of Transportation (SDOT). (2022). Collision Data Dashboard. [https://www.seattle.gov/transportation/](https://www.seattle.gov/transportation/)
4. King County Mobility Coalition. (2020). Mobility Needs Assessment for King County. King County, WA.
