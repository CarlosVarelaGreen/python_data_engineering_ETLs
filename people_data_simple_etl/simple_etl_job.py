""" 
The following python script contains a simple ETL job to extract people data
from multiple sources, including csv, json, and xml. Some based transformations
are performed. At the end, the transformed data gets saved as a csv file ready 
for analysis.
"""
# Importing necessary libraries:
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

# Declaring global file paths:
target_file = 'transformed_data.csv'
log_file = 'log_file.txt'

# Extracting data from sources:
def extract_from_csv(file_to_process):
    df = pd.read_csv(file_to_process)
    return df

def extract_from_json(file_to_process):
    df = pd.read_json(file_to_process, lines=True)
    return df

def extract_from_xml(file_to_process):
    # create empty df to store results: 
    df = pd.DataFrame(columns=["name", "height", "weight"]) 
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root: 
        name = person.find("name").text 
        height = float(person.find("height").text) 
        weight = float(person.find("weight").text) 
        df = pd.concat([df, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True) 
    return df

# Run extraction functions based on filetype:
def extract(): 
    # create an empty df to hold extracted data...
    extracted_data = pd.DataFrame(columns=['name','height','weight'])
     
    # process all csv files:
    for csvfile in glob.glob("*.csv"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 
         
    # process all json files 
    for jsonfile in glob.glob("*.json"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    # process all xml files 
    for xmlfile in glob.glob("*.xml"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data 

# Defining a function to perform transformations on extracted data:
def transform(data): 
    '''Convert inches to meters and round off to two decimals 
    1 inch is 0.0254 meters '''
    data['height'] = round(data.height * 0.0254,2) 
 
    '''Convert pounds to kilograms and round off to two decimals 
    1 pound is 0.45359237 kilograms '''
    data['weight'] = round(data.weight * 0.45359237,2) 
    
    return data

# Loading the final data and logging on to our pipeline:
def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)

def log_process(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second ...
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + ',' + message + '\n')


# Log the initialization of the ETL process :
log_process("ETL Job Started") 
 
# Log the beginning of the Extraction process:
log_process("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process:
log_process("Extract phase Ended") 
 
# Log the beginning of the Transformation process:
log_process("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process:
log_process("Transform phase Ended") 
 
# Log the beginning of the Loading process:
log_process("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process:
log_process("Load phase Ended") 
 
# Log the completion of the ETL process: 
log_process("ETL Job Ended")