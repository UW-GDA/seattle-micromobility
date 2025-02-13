# **Seattle Micromobility: Spatiotemporal Analysis, Safety Hotspots & Geographic Influences** 🚲🛴

**Group members:** Sruangsaeng, Hunter, Ysabel, Alidu

---
 
## 1. Summary
This project investigates **micromobility usage**-specifically e-scooters and bike share in Seattle. Our primary focus is to understand **where** and **when** people ride, locate potential **collision hotspots** involving vulnerable road users (pedestrians, cyclists, e-scooter riders), and examine **geographic factors** (like slope, transit proximity, land use) that may influence both usage and collisions. We hope these insights will guide data-driven enhancements to infrastructure, user behavior, and environmental considerations- ultimately fostering safer and more sustainable micromobility adoption.

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
2. **How** do factors like slope, proximity to transit, or land use affect micromobility usage and collision risk?

**Objectives**
1. **Spatiotemporal Patterns**
    - Identify ridership peaks (daily/weekly/seasonal) and produce usage hotspot maps.
2. **Collision Hotspots**
    - Detect VRU collision clusters using kernel density or Density-Based Spatial Clustering of Applications with Noise (DBSCAN) to compare with usage patterns.
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
        - SDOT Channelization View  
        - Seattle Transportation Plan Bicycle Element  
        - Marked Crosswalks  
        - Beacon Assemblies
    - **🚊 Transit & Traffic Features**  
        - Frequent Transit Service Areas  
        - Streetcar Lines & Stations  
        - Areaways  
        - School Zones  
        - Railroad Crossings  
        - SDOT Intersections  
        - Transportation Table - Seattle Neighborhoods  
        - Current Land Use Zoning Detail
    - **Seattle Open Data Portal**  
🔗 [Seattle Open Data](https://data.seattle.gov)  
    - **🚲 Micromobility Counters**  
        - Spokane St Bridge Bicycle Counter  
        - Thomas St Overpass Bike & Ped Counter  
        - 2nd Ave Cycle Track North of Marion St Bicycle Counter  
        - Elliott Bay Trail in Myrtle Edwards Park Bicycle & Pedestrian Counter  
        - Burke Gilman Trail North of NE 70th St Bicycle & Pedestrian Counter  
        - Fremont Bridge Bicycle Counter  
    - **🌦️ Environmental Data**  
        - Road Weather Information Stations  

3. **Geographic & Slope Data** 🌍  
    - **🔗 [Washington State DNR LiDAR Portal](https://lidarportal.dnr.wa.gov/#45.85941:-120.23438:6)** – High-resolution LiDAR elevation data for slope analysis  
    - **🔗 [Seattle ECA Steep Slope Dataset](https://data-seattlecitygis.opendata.arcgis.com/)** – Identifies areas with slopes ≥40%  

---

## 5. Tools & Packages

* Tools/packages you’ll use (with links)
    * We are going to need to learn how to ingest data from the General Bikeshare Feed Specification ([GBFS](https://gbfs.org/guide/)).
    * Geopandas: https://github.com/geopandas/geopandas
    * Numpy: https://github.com/numpy/numpy
    * Matplotlib: https://github.com/matplotlib/matplotlib
---

## 6. Planned Methodology & Approach

First visualise the data table to find the variables in each dataset. There is the need to determine if the variables are dependant/independant of each other, thus a **correlation analysis** of the variables would be conducted to determine those relations. The variables with positive correlations would be  mapped/visualised to properly appreciate the relationships. **Kernel density mapping** would be used to show hospot areas of high-usage & high correaltion areas for micromobility. The usage patterns would be determined using **geospatial correlations** on slope and land use.

## 7. Expected Outcomes

✔ **Hotspot maps** – High-usage & high-collision areas for micromobility  
✔ **Time-series insights** – Micromobility demand across time periods  
✔ **Geospatial correlations** – Influence of slope & land use on usage patterns  

* Any other relevant information, images/tables, references, etc.

* References
