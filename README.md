# 📈 AWS Finance Data Pipeline

A cloud-based financial data pipeline built with **Python** and **AWS S3**.  
Automates the extraction, processing, and storage of historical stock market data from multiple sources.

---

## 🔍 What it does

1. **Extracts** historical stock data from **Yahoo Finance** (`yfinance`) and **Alpha Vantage** API
2. **Transforms** the raw data by calculating key financial metrics
3. **Loads** the processed results into an **Amazon S3** bucket as CSV files

---

## 📊 Metrics Calculated

| Metric | Description |
|---|---|
| **Daily Return** | Percentage change in closing price day over day |
| **Volatility** | Rolling standard deviation of daily returns |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Data | `yfinance`, `pandas`, `requests` |
| Cloud Storage | AWS S3 via `boto3` |
| External API | Alpha Vantage |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/charleetrion/AWS-Finance-Data-Pipeline.git
cd AWS-Finance-Data-Pipeline
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your credentials

You'll need:
- **AWS credentials** configured locally (`aws configure`) with write access to S3
- **Alpha Vantage API key** — get a free key at [alphavantage.co](https://www.alphavantage.co/support/#api-key)

Set them as environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_REGION=us-east-1
export S3_BUCKET_NAME=your-bucket-name
export ALPHA_VANTAGE_API_KEY=your_api_key
```

### 4. Run the pipeline

```bash
python Script.py
```

The script will download data, calculate metrics, and upload the processed CSV to your S3 bucket.

---

## 📁 Project Structure

```
AWS-Finance-Data-Pipeline/
├── Script.py           # Main pipeline: extract → transform → load
├── requirements.txt    # Python dependencies
└── README.md
```

---

## ☁️ AWS S3 Output

Processed data is saved to S3 in this format:

```
s3://your-bucket-name/
└── finance_data/
    └── processed_AAPL_2024-01-15.csv
```

Each CSV includes: `date`, `open`, `high`, `low`, `close`, `volume`, `daily_return`, `volatility`

---

## 📦 Dependencies

```
yfinance
pandas
boto3
requests
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 💡 Potential Improvements

- [ ] Add AWS Lambda for fully serverless, scheduled execution
- [ ] Use EventBridge to trigger the pipeline daily/weekly automatically
- [ ] Store results in DynamoDB for faster querying
- [ ] Add logging with CloudWatch
- [ ] Dockerize for consistent local execution

---

## 👤 Author

**Carlos Duván Aguirre Rodriguez** — Backend Developer Junior  
[LinkedIn](https://www.linkedin.com/in/carlos-duvan-aguirre-rodriguez-95191b224) · [GitHub](https://github.com/charleetrion)
