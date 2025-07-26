import logging
from etl.extract import extract_data
from config.db_config import create_connection
from etl.transform import transform_data
from etl.load import load_data

# Set up logging ONCE here
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    df = extract_data()
    transform_data(df)
    conn = create_connection()
    load_data()
    

if __name__ == "__main__":
    main()
