""" 
The following python script contains as imple ETL job to extract cars data
from multiple sources, including csv, json, and xml. Some based transformations
are performed. At the end, the transformed data gets saved as a csv file ready 
for analysis."""

# Importing necessary libraries:
import pandas as pd
import glob
import xml.etree.ElementTree as ET
from datetime import datetime
import sys

# Declaring global file paths:
target_file = 'prepared_data.csv'
log_file = 'log_file.txt'
data_source = sys.argv[1] + '/'

# Declaring functions to open and extract raw data:
def open_csv_data(file_to_process):
    df = pd.read_csv(file_to_process)
    return df

def open_json_data(file_to_process):
    df = pd.read_json(file_to_process, lines=True)
    return df

def open_xml_data(file_to_process):
    # Declare initial df:
    df = pd.DataFrame(columns=['car_model', 
                               'year_of_manufacture', 
                               'price', 
                               'fuel'])
    # Parse through xml file:
    tree = ET.parse(file_to_process)
    # Get root:
    root = tree.getroot()
    # Fill in records to df:
    for car in root:
        model = car.find('car_model').text
        year = int(car.find('year_of_manufacture').text)
        price = float(car.find('price').text)
        fuel = car.find('fuel').text
        df = pd.concat([df, pd.DataFrame([{'car_model': model, 
                                           'year_of_manufacture': year,
                                           'price': price, 
                                           'fuel': fuel}])],
                                           ignore_index=True)
    return df

# Define an Extraction pipeline:
def extract(data_source):
    df = pd.DataFrame(columns=['car_model', 
                               'year_of_manufacture', 
                               'price', 
                               'fuel'])
    
    # Stack all data from csv files:
    for csv_file in glob.glob(data_source + "*.csv"):
        df = pd.concat([df, open_csv_data(csv_file)], ignore_index=True)
    
    # Stack all data from json files:
    for json_file in glob.glob(data_source + '*.json'):
        df = pd.concat([df, open_json_data(json_file)], ignore_index=True)

    # Stack all data from xml files:
    for xml_file in glob.glob(data_source + '*.xml'):
        df = pd.concat([df, open_xml_data(xml_file)], ignore_index=True)

    return df

# Apply Transformations:
def round_price(data):
    '''Round the price to two decimals for all records'''
    data['price'] = data['price'].round(2)

    return data

# Loading the transformed data to a target file:
def load_final_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)

    #return None

# Logging pipeline for debugging and control:
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as f:
        f.write(timestamp + ': ' + message + '\n')

    #return None

# Executing pipeline and logging process:
log_progress('Starting ETL pipeline')

# Extracting data from source folder:
log_progress('Data extraction starting...')
extracted_data = extract(data_source)
log_progress('Data extraction completed successfully')

# Transforming data:
log_progress('Transformations starting...')
transformed_df = round_price(extracted_data)
log_progress('Data transformed successfully')
print(transformed_df)

# Loading into target destination:
log_progress("Load phase Started") 
load_final_data(target_file, transformed_df)
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process: 
log_progress("ETL Job Ended Successfully")