""" 
The following python ETL script uses web scraping to extract movies data
from web sources. It uses the requests, beautifulsoup libraries to perform the extraction
of raw data. Then, some transformations are applied. At the end, the transformed data gets
saved both as csv and in a database for analysis.
"""
# Importing the necessary libraries:
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3
import os
from datetime import datetime

# Declaring global variables to be used:
link = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
table_name = 'top_50_movies'
folder_name = 'prepared_data'
target_file = os.path.join(folder_name, 'top_50_films.csv') # to save result as csv
db_name = os.path.join(folder_name,'movies.db')

# Defining a logging function for debugging and control:
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open('log_file.txt', 'a') as f:
        f.write(timestamp + ': ' + message + '\n')

# Use the requests and BeautifulSoup libraries to extract the contents:
log_progress('Starting scraping pipeline')
html_content = requests.get(link).text
raw_data = BeautifulSoup(html_content, 'html.parser')
log_progress('HTML Content retreived')

# Find all the relevant tables:
tables = raw_data.find_all('tbody')
log_progress('Finding table records')
# Accessing data from the first table (desired):
table_rows = tables[0].find_all('tr')
# Looping over rows to get data:
record_number = 0
final_df = pd.DataFrame(columns=['Average Rank',
                                 'Film',
                                 'Year'])
for row in table_rows:
    if record_number<50: #to get top 50...
        attributes = row.find_all('td')
        if len(attributes)!=0: #if there are columns...
            # Get the desired column info only:
            record = {
                "Average Rank": attributes[0].contents[0],
                "Film": attributes[1].contents[0],
                "Year": attributes[2].contents[0]
            }
            records_df = pd.DataFrame(record, index=[0])
            final_df = pd.concat([final_df, records_df], ignore_index=True)
            record_number+=1 # increment counter for top 50 records
    else:
        break
log_progress('All records obtained')

#Save the extracted information in the required formats:
log_progress('Saving data to csv file')
if not os.path.exists(folder_name):
    os.makedirs(folder_name)  # This will create our folder to store final data...

# Save prepared data to directory:
final_df.to_csv(target_file, index=False)

# Initialize connection to sqlite db:
log_progress(f'Saving data to database inside {db_name} directory')
conn = sqlite3.connect(db_name)
final_df.to_sql(table_name, conn, if_exists='replace', index=False) #Replace since we only want top 50
conn.close() # close connection to end session

log_progress('Scraping job ended')