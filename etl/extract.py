import pandas as pd
import logging

def extract_data():
    logging.info("Extracting data from CSV...")
    df = pd.read_csv("data/social_media_engagement1.csv")
    logging.info("Data extracted successfully.")
    return df
