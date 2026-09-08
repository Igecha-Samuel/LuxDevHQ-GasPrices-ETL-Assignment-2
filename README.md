# LuxDevHQ-GasPrices-ETL-Assignment-2

## Project Overview

With this project i implemented an ETL  pipeline with the data being sourced from the CollectAPI Gas Price API and then stored in a postgresql database.

## Project Strcuture

```
Gas ETL Assignment/
├── data/
│   ├── gas_prices.csv/          # Raw gas prices
├── .py fles/              # Source code
│   ├── extract.py
│   ├── load.py
│   ├── Transform.py
│   ├── main.py
│   └── pipeline.py
├── requirements.txt
└── README.md
```

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```