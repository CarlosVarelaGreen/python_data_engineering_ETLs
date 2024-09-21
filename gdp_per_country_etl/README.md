# GDP per Country ETL python pipeline

### Overview
The "GDP per Country ETL" project extracts data from a web page, transforms it into a structured format, and loads the data into both a JSON file and an SQLite database. This project demonstrates how to scrape data from a Wikipedia page listing countries by GDP and automate the ETL process.

### Steps in the ETL Pipeline

#### Extract:
The script scrapes data from a Wikipedia page about countries and their GDP using Python's requests and BeautifulSoup libraries.
The relevant table containing GDP data is identified and parsed into a Pandas DataFrame.

#### Transform:
The GDP values are cleaned, converting them from strings into numerical values.
The GDP data is transformed to billions (USD) and rounded to two decimal places.

#### Load:
The transformed data is saved into two target locations:
As a JSON file in the prepared_data folder.
As a table in an SQLite database located in the prepared_data directory.

### Directory Structure
prepared_data: Contains the transformed data, including the JSON file and the SQLite database.
log_data: Stores log files to track the progress and success of each step in the ETL process.

### Key Files
gdp_per_country_etl.py: The main Python script that runs the ETL process.
etl_project_log.txt: A log file recording progress and any errors encountered during the process.
World_Economies.db: The SQLite database that holds the Countries_by_GDP table.

### Requirements
Python 3.x
Libraries: pandas, requests, beautifulsoup4, sqlite3
You can install the required libraries using:
pip install -r requirements.txt

### Running the Project
To run the project, simply execute the main Python script:
python gdp_per_country_etl.py
This will scrape, transform, and store the data, and log the progress in the etl_project_log.txt file.

### Summary of Output:
Countries_by_GDP.json: JSON file containing the list of countries and their respective GDP.
SQLite Database: The data is also stored in a database table Countries_by_GDP.
