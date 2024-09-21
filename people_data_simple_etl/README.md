# People Data Simple ETL

This repository contains a simple ETL (Extract, Transform, Load) job that processes people data from multiple sources including CSV, JSON, and XML files. Basic transformations are applied, and the final transformed data is saved in CSV format for analysis.

## Project Overview

The **People Data Simple ETL** project demonstrates how to extract data from various file formats, perform basic transformations (such as unit conversions), and store the transformed data for analysis. This ETL process provides a structured and cleaned dataset ready for further data exploration and analytics.

## ETL Pipeline Phases

### 1. Extract
The pipeline extracts data from three different file formats:
- **CSV**: All CSV files in the current directory are processed.
- **JSON**: All JSON files in the current directory are processed.
- **XML**: All XML files in the current directory are processed.

Each file is parsed and data related to people's names, height, and weight is extracted.

### 2. Transform
The transformations applied to the extracted data include:
- **Converting height from inches to meters**: Since the raw data contains heights in inches, this is converted to meters using the conversion factor `1 inch = 0.0254 meters`.
- **Converting weight from pounds to kilograms**: The weight data, originally in pounds, is converted to kilograms using the factor `1 pound = 0.45359237 kilograms`.

The transformed data is rounded to two decimal places for better readability.

### 3. Load
The transformed data is saved as:
- **CSV**: The processed data is saved in a CSV file named `transformed_data.csv`.

## Directory Structure

- **people_data_simple_etl.py**: The main Python script containing the ETL pipeline.
- **transformed_data.csv**: The output CSV file containing the cleaned and transformed data.
- **log_file.txt**: A log file that tracks the progress of the ETL process from extraction to loading.

## How to Run

### Prerequisites
Ensure you have Python 3.x installed, along with the following required libraries:
- `pandas`
- `glob`
- `xml.etree.ElementTree`

You can install the required libraries by running:

`pip install pandas`

## Usage

1. Clone this repository or download the script.
2. Place your CSV, JSON, and XML files in the same directory as the script.
3. Run the ETL script from the command line:

   `python people_data_simple_etl.py`

The script will log its progress in log_file.txt and output the transformed data into transformed_data.csv.

### Output Files
- CSV File: transformed_data.csv — Contains the final transformed data (height in meters, weight in kilograms).
- Log File: log_file.txt — Tracks all key steps of the ETL process including extraction, transformation, and loading.

## Logging
The ETL pipeline logs each significant step in the log_file.txt file. This includes information about:

- Initialization of the ETL process
- Start and end of the extraction phase
- Start and end of the transformation phase
- Start and end of the loading phase
- Completion of the entire ETL job
This ensures transparency and helps in debugging if any issues arise during the execution of the ETL process.

### Example of Transformed Data
The output dataset saved in the CSV file will look like the following:

| Name       | Height (m) | Weight (kg) |
|------------|-------------|-------------|
| John Doe   | 1.75        | 70.31       |
| Jane Smith | 1.60        | 55.00       |


## Future Enhancements
Add support for other data formats such as Excel or Google Sheets.
Improve logging by adding error-handling mechanisms for different file formats.
Include additional data validation and cleaning steps.

