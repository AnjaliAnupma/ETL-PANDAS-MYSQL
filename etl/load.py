import pandas as pd
from config.db_config import create_connection
import mysql.connector
from mysql.connector import Error 
import logging

def load_data():
    try:
        # Read transformed CSV
        df = pd.read_csv('transformed.csv')

        # Connect to DB
        conn = create_connection()
        cursor = conn.cursor()

        # Create table if not exists
        create_table_query = """
        CREATE TABLE IF NOT EXISTS posts (
            post_id INT,
            platform VARCHAR(100),
            post_type VARCHAR(100),
            post_date DATE,
            post_day VARCHAR(20),
            post_timing TIME,
            likes INT,
            comments INT,
            shares INT
        );
        """
        cursor.execute(create_table_query)

        # Insert data
        for _, row in df.iterrows():
            insert_query = """
            INSERT INTO posts (
                post_id, platform, post_type, post_date, post_day,
                post_timing, likes, comments, shares
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, tuple(row))


        # insert_query = """
        # INSERT INTO posts (
        #     post_id, platform, post_type, post_date, post_day,
        #     post_timing, likes, comments, shares
        # )
        # VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        # """
        # cursor.executemany(insert_query, [tuple(x) for x in df.values])

        conn.commit()
        logging.info("Data loaded into MySQL successfully!")
        cursor.close()
        conn.close()
        logging.info("Closed DB connection!")
    except Error as e:
        logging.error(f"Not able to load in db. Error: {e}")



