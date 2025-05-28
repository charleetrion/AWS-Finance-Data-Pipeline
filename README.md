# AWS Finance Data Pipeline

This project implements a financial data processing pipeline in the cloud using AWS services. The pipeline downloads, processes, and saves historical financial data from various sources such as Yahoo Finance and Alpha Vantage, calculating key metrics such as daily returns and volatility. The processed data is stored in an Amazon S3 bucket, facilitating subsequent analysis and integration with other applications.

The purpose of this project is to offer a scalable, efficient, and automated solution for managing financial data using the AWS infrastructure.

## Description

This pipeline allows for automated and efficient financial data management, covering the following stages:

### 1. **Financial Data Collection**
- Historical data on financial assets is downloaded from two main sources:
- **Yahoo Finance** via the `yfinance` library. This API provides real-time historical data on stocks, funds, and other financial assets.
- **Alpha Vantage**, using a free API that offers detailed data on stock, forex, and cryptocurrency markets.

### 2. **Data Processing**
- Once the data is downloaded, it is processed to calculate **key financial metrics**:
- **Daily Return**: Calculates the daily percentage change in the stock price.
- **Volatility**: Measures the variability of stock prices over time.
- These calculations are performed on the closing price or adjusted stock price columns.

### 3. **S3 Storage**
- The processed data (including calculated returns and volatility) is stored in a CSV file.
- This CSV file is automatically uploaded to an **Amazon S3** bucket, providing a secure, durable, and accessible place for further analysis.

### 4. **Scalability and Automation**
- This pipeline is designed to easily scale with more stock tickers or longer time periods.
- The use of services like **Amazon S3** and the automation of the process make it suitable for real-time analysis, periodic reporting, or integrations with other systems.

### Requirements

To run this project, you must have the following configured:

- **Python 3.x**: The project is developed in Python 3.x, so you must have this version installed in your environment.

- **Python Packages**: The project uses several libraries, which you can install using `pip`:
- `yfinance`: For downloading historical data from Yahoo Finance.
- `pandas`: For data manipulation and financial analysis.
- `boto3`: For interacting with AWS (S3) services.
- `requests`: For making HTTP requests to the Alpha Vantage API.

#### Install Dependencies
Install the required dependencies:
- pip install -r requirements.txt
