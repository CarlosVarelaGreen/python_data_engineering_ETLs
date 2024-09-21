# importing necessary libraries:
import pandas as pd
import glob
import os
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import sqlite3

# Declaring global variables:
target_directory = 'prepared_data'
target_file = os.path.join(target_directory, 'Countries_by_GDP.json')
log_directory = 'log_data'
log_file = os.path.join(log_directory, 'etl_project_log.txt')
db_name = os.path.join(target_directory, 'World_Economies.db')
table_name = 'Countries_by_GDP'
data_url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

# Creating directories:
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# creating log function for debugging and control:
def log_progress(message):
    """ this function logs the progress of this script
        into a txt file called etl_project_log.txt
        inside a log folder"""
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as f:
        f.write(timestamp + ': ' + message + '\n')

# Extracting raw data from website:
log_progress('Requesting website information')

def webscraper(url):
    """This function scrapes a specific table from the given URL
    and stores the records inside a pandas dataframe."""
    try:
        html_content = requests.get(url).text
        raw_data = BeautifulSoup(html_content, 'html.parser')

        # Finding the table by its class
        log_progress('Finding the specific table by class')
        table = raw_data.find('table', {'class': 'wikitable'})
        
        # If the table is not found, log and return an error:
        if not table:
            log_progress('Failed to find the table with the given class')
            return "Table not found"
        
        log_progress('Extracting table data')
        
        # Extracting the rows from the found table:
        gdp_table = table.find('tbody').find_all('tr')
        
        # Initializing dataframe outside the loop:
        gdp_df = pd.DataFrame(columns=['Country', 'GDP_USD_billion'])

        # Loop through the table rows:
        for row in gdp_table:
            attributes = row.find_all('td')
            
            # Check if there are enough columns to extract:
            if len(attributes) >= 3:
                try:
                    record = {
                        'Country': attributes[0].get_text(strip=True),
                        'GDP_USD_billion': attributes[2].get_text(strip=True)
                    }
                    record_df = pd.DataFrame([record])  # Transform record into DataFrame
                    gdp_df = pd.concat([gdp_df, record_df], ignore_index=True)  # Append loop results
                except Exception as row_error:
                    log_progress(f"Error processing row: {row_error}")
            else:
                log_progress(f"Skipping row with insufficient data: {attributes}")
        
        return gdp_df
    
    except Exception as e:
        log_progress(f'Failed to extract HTML content: {e}')
        return f"An error occurred: {e}"

# Transforming scraped data:
def transform_data(extracted_df):
    # Convert the 'GDP_USD_billion' column to numeric:
    log_progress("Converting strings to numbers")
    extracted_df['GDP_USD_billion'] = pd.to_numeric(extracted_df['GDP_USD_billion'].str.replace(',', ''), 
                                                    errors='coerce')
    # Convert the 'GDP_USD_billion' to actual billion values rounded to 2 decimals:
    extracted_df['GDP_USD_billion'] = round((extracted_df['GDP_USD_billion'] * 0.001),2)
    log_progress("converting to billions and rounding values")
    
    return extracted_df

# Loading to target sources:
def load_data(final_df):
    log_progress(f'Saving data to {target_directory} directory as {target_file}')
    final_df.to_json(target_file)

    # Initialize connection to sqlite db:
    log_progress(f'Saving data to database {db_name} inside table {table_name}')
    conn = sqlite3.connect(db_name)
    final_df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close() # close connection to end session

    return "Data saved successfully"


def main():
    log_progress('Starting the scraping job')
    
    # Extracting data from source:
    gdp_raw_df = webscraper(data_url)
    if isinstance(gdp_raw_df, str):  # Check if there was an error
        log_progress(gdp_raw_df)
        return
    # Logging extraction success:
    log_progress("Successfully extracted data from source")
    
    # Transforming data for destination:
    transformed_gdp_df = transform_data(gdp_raw_df)
    log_progress("Successfully transformed data")
    
    # Loading final data to target sources:
    load_data(transformed_gdp_df)

    log_progress('Scraping job ended successfully')

if __name__ == "__main__":
    main()
