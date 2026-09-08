import pandas as pd

def transform_gas_prices(cities):

    cities_df = pd.DataFrame(cities)

    cities_df.drop(columns=['lowername'],inplace=True)

    cities_df.rename(columns={'name':'cities'}, inplace=True)

    return cities_df