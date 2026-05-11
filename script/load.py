from loguru import logger
import pandas as pd
from datetime import datetime
def load(df):
    '''This function loads the transformed employee DataFrame into a CSV file.
    It includes error handling to log any issues that occur during the loading process.'''
    
    if df is None:
        return None
    try:
        logger.info("loading data...")
        df.to_csv('data/processed/employee_data.csv', index=False)
    except Exception as e:
        logger.error(f'Error during loading: {e}')
        raise e 