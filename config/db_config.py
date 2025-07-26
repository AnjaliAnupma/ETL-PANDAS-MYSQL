import logging
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Load .env file
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}


def create_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            logging.info("Connection to MySQL DB successful")
        return connection
    except Error as e:
        logging.error(f"Error: {e}")
        return None
