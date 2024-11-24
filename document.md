# Global Solution - Green Energy: Optimizing Energy Consumption Using Weather Data

**Team Member:** [Luis Emidio RM559976](https://www.linkedin.com/in/luisfuturist)

> This project is part of the **Artificial Intelligence** course at [FIAP](https://github.com/fiap) - Online 2024. It serves as the **Global Solution - Green Energy** project.

The project involves selecting three items from the provided project instructions. We chose the following:

- Artificial Intelligence Challenges (AIC)  
- Cognitive Data Science (CDS)  
- Go Beyond  

Project files can be accessed in the `./files` directory on the FIAP Platform submission or via GitHub: [GS-Green](https://github.com/luisfuturist/gs-green).

---

## Abstract

This project focuses on optimizing energy consumption by analyzing weather data. Publicly available energy consumption data from the Brazilian Energy Regulatory Agency (ANEEL) and weather data from OpenWeatherMap are used to develop a solution that identifies opportunities for improvement. This document outlines the data acquisition, processing steps, and the expected outcomes of our solution.

---

## 1. Introduction

### **1.1 Context**  
Global energy consumption significantly contributes to environmental challenges. Optimizing energy usage is crucial to mitigating climate change and promoting sustainable development. Brazil’s diverse energy landscape provides an excellent case study for exploring energy efficiency strategies.  

### **1.2 Objectives**  
The primary goal of this project is to develop a system that accurately records energy consumption in Brazil and identifies optimization strategies. This involves using publicly available data, implementing advanced analytics, and exploring the potential of AI and IoT technologies.  

### **1.3 Challenges**  
Key challenges include acquiring and processing large datasets from multiple sources. Ensuring data quality, handling missing values, and managing inconsistencies are critical. Additionally, building real-time integrations that account for factors like weather, seasonal variations, and consumption patterns presents a significant technical hurdle.  

### **1.4 Barriers**  
Data limitations, such as incomplete or insufficiently granular datasets, can affect solution accuracy. Integrating IoT devices for real-time data collection may require substantial infrastructure investment. Furthermore, ensuring data privacy and security is essential.  

---

## 2. Development

### **2.1 Data Acquisition**  

- **ANEEL Data:** Historical energy consumption data was retrieved from ANEEL's open data API. Metrics include total consumption, sector-specific data, and tariff classifications. The data was stored in a PostgreSQL database.  
- **OpenWeatherMap Data:** Weather data (e.g., temperature, humidity, wind speed) was obtained from OpenWeatherMap's API. This data was used to explore correlations with energy consumption patterns, improving solution accuracy.  

### **2.2 Data Processing and Storage**  

- **Database:** A PostgreSQL database was used to store and manage energy consumption data for efficient analysis and retrieval.  
- **Data Cleaning:** Raw data was preprocessed to handle missing values, outliers, and inconsistencies. Transformations such as normalization and scaling were applied to ensure compatibility with our solution.  

### **2.3 Analysis Scripts**  

Python scripts were developed to analyze data stored in the PostgreSQL database. The script `analyse_data.py` calculates per capita consumption and identifies trends. Results are visualized for reporting purposes. Future iterations may include more advanced time series analysis.

---

## 3. Expected Results

### **3.1 Energy Savings**  
Optimized energy consumption settings, informed by weather data, are expected to reduce energy use. For instance, external temperature data can trigger notifications for adjustments, such as turning off lights when unnecessary.  

### **3.2 Impact on Comfort**  
Real-time weather data enables proactive appliance adjustments (e.g., pre-cooling or heating), maintaining comfort while minimizing energy waste.  

### **3.3 Equipment Usage**  
Optimized settings are likely to reduce compressor runtimes in household utilities, decreasing wear and tear on equipment.  

### **3.4 Lifespan Improvement**  
Reduced operational stress on household utilities could potentially extend their lifespan. This long-term effect warrants further investigation.  

### **3.5 Data Visualization**  
Future plans include interactive dashboards displaying real-time predictions, regional consumption patterns, and weather overlays. Scenario planning tools will also simulate optimization strategies.  

---

## 4. Conclusion  

This project demonstrates the potential of technology to optimize energy consumption. The proposed solution offers accurate energy usage insights, enabling targeted interventions for reduction. Further research could focus on integrating real-time data and incorporating additional factors, such as user behavior, to enhance efficiency.  

Although limitations such as data availability and integration complexity exist, the project shows promise in achieving significant energy savings and improving sustainability through smart energy management. Future work will address these limitations by adding new data sources, enhancing performance, and improving real-time integration.  
