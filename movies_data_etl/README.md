# Movies Data ETL Pipeline
This repository contains an ETL (Extract, Transform, Load) pipeline designed to extract movie data from web sources using web scraping. The pipeline extracts data from an archived webpage, applies transformations, and stores the processed data both in CSV format and in a SQLite database for further analysis.

## Project Overview
The Movies Data ETL project demonstrates how to scrape data from web sources and process it into a structured format for analysis. The project focuses on scraping the top 100 highest-rated films, transforming the data, and saving the top 25 films released after the year 1999.

## ETL Pipeline Phases
### Extract
The pipeline scrapes movie data from the following source:

100 Most Highly-Ranked Films (archived)
It retrieves the top 100 films listed on the page, focusing on film name, year of release, and ranking based on Rotten Tomatoes' Top 100.

### Transform
Filter Movies Released After 1999: The script filters the scraped data to only include films released in the year 2000 or later.
### Load
The transformed data is saved in two formats:

- CSV: The top 25 movies released after 1999 are saved as a CSV file in the prepared_data folder.
- SQLite Database: The same data is stored in a SQLite database in the same folder.

## Directory Structure
- movies_data_etl.py: The main Python script that contains the ETL pipeline.
- prepared_data: Folder where the processed CSV file and the SQLite database are saved.
- log_file_200.txt: A log file that tracks the progress of the ETL process, including scraping, transformation, and saving phases.

## How to Run
### Prerequisites
Ensure you have Python 3.x installed, along with the necessary libraries:

- beautifulsoup4
- requests
- pandas
- sqlite3
You can install the required libraries by running:

*pip install beautifulsoup4 requests pandas*

## Usage
1. Clone this repository or download the script.
2. Run the ETL script from the command line: 
    python movies_data_etl.py

The script will log its progress in log_file_200.txt and output the transformed data into the prepared_data folder.

### Output Files
- CSV File: prepared_data/top_25_films.csv — Contains the top 25 movies released after 1999.
- SQLite Database: prepared_data/movies.db — Stores the same data in a SQLite database table named top_25_movies.

## Logging
The ETL pipeline logs each significant step in the log_file_200.txt file. This includes information about:

- Starting the scraping process
- Retrieving the HTML content
- Processing movie records
- Filtering data to include only movies released after 1999
- Saving the final dataset to CSV and SQLite
This ensures transparency and aids in debugging any issues encountered during execution.