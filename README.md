# Integrating Public Transportation and Air Quality Data for Urban Planning in Abu Dhabi

## Overview
This project aims to integrate public transportation usage data with air quality index data to optimize urban planning in Abu Dhabi. This integration allows for the analysis of how public transit influences air quality and provides insights for improving both transportation efficiency and environmental health.

## Datasets
- **Public Transportation Usage Dataset**: Provides statistics on ridership, peak usage times, and route popularity.
- **Air Quality Index Dataset**: Contains data on pollutants such as PM2.5, PM10, NO2, CO, and O3.

## Objective
- Optimize bus and metro schedules based on peak usage times.
- Identify underutilized routes for potential service changes.
- Assess the impact of public transport on reducing emissions and improving air quality.

## Prerequisites
- Python 3.x
- Pandas library for data manipulation
- Matplotlib for data visualization

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/yourusername/abu-dhabi-urban-planning.git
   
2. Navigate to the project directory:
   bash
   cd abu-dhabi-urban-planning
   
3. Install the required Python packages:
   bash
   pip install pandas matplotlib
   

## Usage
1. Ensure the datasets are in the project directory:
   - `public_transport_usage_2020.csv`
   - `air_quality_index_2020.csv`

2. Run the analysis script:
   bash
   python analysis.py
   

3. The script will output the correlation between ridership and PM2.5 levels and plot a graph of public transport ridership vs air quality.

## Contribution
Feel free to open issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
