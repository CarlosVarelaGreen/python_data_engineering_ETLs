# ETL Projects Repository

Welcome to the ETL Projects Repository! This collection contains four distinct Python scripts designed for ETL (Extract, Transform, Load) tasks. Each project demonstrates how to extract data from various sources, perform transformations, and load the results into structured formats for analysis.

## Projects Overview

### 1. **car_prices_etl**
- **Description**: This ETL job extracts car data from multiple formats (CSV, JSON, XML), applies basic transformations, and saves the cleaned data into a CSV file ready for analysis.
- **Key Features**:
  - Supports multiple input data formats.
  - Data transformation, including rounding prices.
  - Progress logging throughout the ETL process.

### 2. **gdp_per_country_etl**
- **Description**: The "GDP per Country ETL" project extracts data from a web page, transforms it into a structured format, and loads the data into both a JSON file and an SQLite database. This project demonstrates how to scrape data from a Wikipedia page listing countries by GDP and automate the ETL process.
- **Key Features**:
  - Supports web scraping.
  - Data transformation, including conversion from millions to billions.
  - Data Wrangling: The GDP values are cleaned, converting them from strings into numerical values. 
  - Progress logging throughout the ETL process.

### 3. **movies_data_etl**
- **Description**: This script scrapes data about the top 50 and 25 films from a web source. It transforms the data by filtering movies released after the year 2000 and saves the final results in both CSV and SQLite database formats.
- **Key Features**:
  - Web scraping using BeautifulSoup and Requests.
  - Data filtering and transformation.
  - Logging of key ETL steps.

### 4. **people_data_simple_etl**
- **Description**: This project extracts people data from CSV, JSON, and XML files, converting height from inches to meters. The transformed data is saved as a CSV file.
- **Key Features**:
  - Multi-format data extraction.
  - Basic data transformation and conversion.
  - Logging of ETL processes.

## Usage

To utilize any of the projects, follow these steps:

1. **Clone this repository** or download the scripts directly.
2. **Go through the documentation** Access the readme file from each project to learn more.
3. **Install dependencies** Make sure to 
4. **Run the desired ETL script** from the command line:
   ```bash
   python <script_name>.py

## Summary of Dependencies by Project
### movies_data_etl:

- pandas
- requests
- beautifulsoup4
- lxml (optional)

### people_data_simple_etl:

- pandas
- lxml (optional, if parsing XML)

### car_prices_etl:

- pandas
- requests
- lxml (optional, if parsing XML)

### gdp_data_etl (hypothetical project using web scraping):

- pandas
- requests
- beautifulsoup4
- lxml (optional)

## Future Enhancements
We welcome contributions to improve these projects. Potential enhancements include:

- Support for additional data formats (e.g., Excel, Google Sheets).
- Enhanced error handling and logging mechanisms.
- Additional data validation and cleaning steps.
- Support for job orchestration
- Idempotency assessment
- Automation