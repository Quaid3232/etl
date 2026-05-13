import pandas as pd
from numpy import select
import psycopg2
from psycopg2.extras import execute_values
from loguru import logger


def load(transfromed_df):
    'This function load transformed data into datawarehouse'
    if transfromed_df is None:
        return None
    logger.warning(f'Data loading stop due to transfromed_df is none')

    con = None
    cur = None

    try:
        logger.info("Loading data into PostgreSQL...")
        con=psycopg2.connect(
            database='pw',
            user='postgres',
            password=321,
            host='localhost')

        cur = con.cursor()
        insert_query = ''' INSERT INTO
        employee (employeeID,name,age,department,salary,joinDate,tenure_year) 
        values (%s,%s,%s,%s,%s,%s,%s )'''

        # execute_values(cur, insert_query, transfromed_df.values.tolist())
        cur.executemany(insert_query, transfromed_df.values.tolist())
        con.commit()
        logger.info("Data loaded successfully into PostgreSQL.")
    except Exception as e:
        logger.error(f'database connection error: {e}')
    finally:
        if con:
            con.close()
        if cur:
            cur.close()

# # loading bad record 
#     if bad_df is None:
#         return None
#     try:
#         logger.info("loading bad data...")
#         date_str = datetime.now().strftime("%Y-%m-%d")
#         bad_df.to_csv(f'data/quarantine/employee_data_{date_str}.csv', index=False)
#     except Exception as e:
#         logger.error(f'Error during loading: {e}')
#         raise e 
#     logger.info("bad data loading finished...")
