# Global Solution - Green Energy: Optimizing Energy Consumption using Weather Data

**Team Members:** [Luis Emidio RM559976](https://www.linkedin.com/in/luisfuturist)

> This project is part of the **Artificial Intelligence** course at [FIAP](https://github.com/fiap) - Online 2024. This project is the **Global Solution - Green Energy**.

It consists of a selection of three items from the project instructions. We have chosen the following items:

- Artificial Intelligence Challenges (AIC)
- Cognitive Data Science (CDS)
- Go Beyond

You can access the project files in the `./files` directory on the FIAP Platform submission or on GitHub at: [GS-Green](https://github.com/luisfuturist/gs-green).

## Abstract

This project explores the optimization of energy consumption using the analysis of weather data. We leverage publicly available energy consumption data from the Brazilian Energy Regulatory Agency (ANEEL) and weather data from OpenWeatherMap to develop a solution that identifies potential areas for improvement. This document details the data acquisition, processing, and expected results of our solution.

## 1. Introduction

**1.1 Context:** Global energy consumption is a significant contributor to environmental challenges. Optimizing energy usage is crucial for mitigating climate change and promoting sustainable development. Brazil, with its vast and diverse energy landscape, presents a prime case study for exploring energy efficiency improvements.

**1.2 Objectives:** Our primary objective is to develop a system that accurately register energy consumption in Brazil and identifies strategies for optimization. This involves leveraging publicly available data, implementing advanced analytics, and exploring the potential of AI and IoT technologies.

**1.3 Challenges:** Acquiring and processing large datasets from diverse sources presents a significant challenge. Ensuring data quality, handling missing values, and managing data inconsistencies requires careful consideration. Developing real-time integration that account for various factors (weather, seasonal variations, consumption patterns) is another key challenge.

**1.4 Barriers:** Data limitations (e.g., incomplete datasets, lack of granular data) can impact the solution. The integration of IoT devices for real-time data acquisition may require significant infrastructural investments. Ensuring data privacy and security is also a crucial consideration.

## 2. Development

### 2.1 Data Acquisition

* **ANEEL Data:** We utilized the ANEEL open data API to retrieve historical energy consumption data for Brazil. This data includes various metrics, such as total energy consumption, consumption by sector, and tariff classifications. The data was initially stored in a relational database (PostgreSQL).
* **OpenWeatherMap Data:** Weather data (temperature, humidity, wind speed, etc.) from OpenWeatherMap API were incorporated to explore correlations with energy consumption patterns. This data is crucial for improving the accuracy of the solution.

### 2.2 Data Processing and Storage

* **Database:** A PostgreSQL database was used to store and manage the energy consumption. This allows for efficient data retrieval and analysis.
* **Data Cleaning:** The raw data underwent preprocessing steps to handle missing values, outliers, and inconsistencies. Data transformations (e.g., normalization, scaling) were performed as needed for our solution.

### 2.3 Analysis Scripts

Python scripts analyze data from the PostgreSQL database. `analyse_data.py` calculates per capita consumption and identifies trends. Results are visualized for the report. More advanced time series analysis could be added.

## 3. Results Expected

- **3.1 Energy Savings:** We anticipate a reduction in energy consumption for utilities through optimized settings based on reactivity of external temperature and weather data. This is based on the ability to accurately notify the need for adjustments, such as turning off the lights.

- **3.2 Impact on Comfort:** Real-time weather data allows proactive appliance adjustments (pre-cooling/heating), maintaining comfort by mitigating the impact of temperature swings and reducing energy waste.

**3.3 Equipment Use:** Optimized settings will likely lead to reduced compressor runtime for the household utilities, decreasing wear and tear on the equipment.

**3.4 Lifespan:** Reduced stress on the household utilities due to optimized operation may potentially extend its lifespan. This is a longer-term effect requiring further investigation.

**3.5 Data Visualization:** Future plans include interactive dashboards visualizing real-time predictions and regional consumption patterns, overlaid with weather data, and scenario planning tools to simulate optimization strategies.

## 4. Conclusion

This project successfully demonstrated the potential of Technology in optimizing energy consumption. Our solution idea provides accurate reading of energy usage, allowing for targeted interventions to reduce consumption. Further research could focus on integrating real-time data for more refined implementation and incorporating additional factors (e.g., user behavior) to enhance the efficiency. The results suggest a significant potential for energy savings and improved sustainability through smart energy management. The limitations of this project are data availability and integration complexity. Future work will include steps such as adding new data sources, improving performance and real-time integration.
