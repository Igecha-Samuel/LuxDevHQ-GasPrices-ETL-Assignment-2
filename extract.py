import http.client
import json
import os
import pandas as pd
from dotenv import load_dotenv

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