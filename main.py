import pandas as pd
from loguru import logger
from datetime import datetime

from script.extract import extraction
from script.transform import data_transformation
from script.load import load
from dbutil.db import path
def main():
    '''This is the main function that orchestrates the ETL process for employee data.
    It calls the extraction, transformation, and loading functions in sequence,
    and includes error handling to log any issues that occur during the process.'''
    
    try:
        df = extraction(path)
        
        # Transform data
        transfromed_df = data_transformation(df)
        
        # Load data
        load(transfromed_df)
        
    except Exception as e:
        logger.error(f'Error in ETL process: {e}')
        raise e

if __name__ == "__main__":
    main()