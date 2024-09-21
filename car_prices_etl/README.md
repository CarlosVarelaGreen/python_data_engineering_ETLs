# Car Prices ETL Pipeline
This repository contains an ETL (Extract, Transform, Load) pipeline that processes car pricing data from multiple data sources, including CSV, JSON, and XML files. The pipeline extracts raw data, applies basic transformations, and loads the transformed data into a CSV file ready for analysis.

## Project Overview
The Car Prices ETL project demonstrates how to handle data from diverse sources by extracting and merging data from multiple formats into a unified dataset. The project also includes basic data transformations like rounding prices to two decimal places, followed by loading the final dataset into a CSV file.

### ETL Pipeline Phases
1. Extract
The pipeline supports three data formats:

- CSV: Comma-separated value files.
- JSON: Line-separated JSON files.
- XML: XML files with car data.

The script scans the input directory for all files of these formats and loads them into a single Pandas DataFrame.

2. Transform
The following transformation is applied:

Price Rounding: The car prices are rounded to two decimal places for consistency.
3. Load
The transformed data is saved to a CSV file named prepared_data.csv. This file contains a unified dataset with the following columns:

- car_model: The model of the car.
- year_of_manufacture: The year the car was manufactured.
- price: The price of the car (rounded to two decimal places).
- fuel: The type of fuel used by the car.

### Directory Structure
car_prices_etl.py: The main Python script that contains the ETL pipeline.
log_file.txt: A log file that tracks the progress of the ETL process, including extraction, transformation, and loading phases.

### How to Run
#### Prerequisites
Ensure you have Python 3.x installed, along with the necessary libraries:

- pandas
- xml.etree.ElementTree
You can install the required libraries by running:
pip install pandas

### Usage
Place all your data files (CSV, JSON, and XML) into a folder.
Run the ETL script from the command line, passing the folder path as an argument. For example:
*python car_prices_etl.py /path/to/data_folder*

The script will log its progress in log_file.txt and output the transformed data to prepared_data.csv.

### Example Files Supported
CSV: Contains columns like car_model, year_of_manufacture, price, fuel.
JSON: Line-separated JSON with the same fields.
XML: Car data structured with tags like <car_model>, <year_of_manufacture>, <price>, and <fuel>.

### Logging
The ETL pipeline logs every major step and any errors encountered during the extraction, transformation, and load phases. This helps in debugging and tracking the progress of the ETL job. The logs are saved in log_file.txt.