import http.client
import json
import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()  

def extract_gas_prices():
    api_key = os.getenv("GAS_API")

    if not api_key:
        raise ValueError("GAS_API not found in .env")

    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': f"apikey {api_key}"
        }

    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

    parsed_data = json.loads(data.decode("utf-8"))

    cities = parsed_data['result']['cities']

    return cities

def transform_gas_prices(cities):

    cities_df = pd.DataFrame(cities)

    cities_df.drop(columns=['lowername'],inplace=True)

    cities_df.rename(columns={'name':'cities'}, inplace=True)

    return cities_df

def load_gas_prices(cities_df):

    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    cities_df.to_sql('gas_prices', con=engine, if_exists='replace', index=False)

def main():
    cities = extract_gas_prices()
    cities_df = transform_gas_prices(cities)
    load_gas_prices(cities_df)

    print('ETL process completed successfully')


if __name__ == "__main__":
     main()
