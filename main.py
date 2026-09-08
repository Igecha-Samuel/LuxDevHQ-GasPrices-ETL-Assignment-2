from extract import extract_gas_prices
from transform import transform_gas_prices
from load import load_gas_prices


def main():
    cities = extract_gas_prices()
    cities_df = transform_gas_prices(cities)
    load_gas_prices(cities_df)

    print('ETL process completed successfully')


if __name__ == "__main__":
     main()