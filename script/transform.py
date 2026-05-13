import pandas as pd
from loguru import logger
from datetime import datetime

def data_transformation (df):
    '''This function performs data transformation on the employee DataFrame.
    It includes cleaning, formatting, and calculating tenure for each employee.
    The function also logs the total records before and after transformation,
    as well as any errors encountered during the process.'''
    
    if df is None:
        return None
    try:    
        logger.info("transforming data...")
        # total record
        total_record = df['employeeID'].count()
        logger.info(f'total records : {total_record}')

        # remove extra spacing and title
        df['name'] = df['name'].str.title().str.strip()

        # remove extra spacing and upper 
        df['department']= df['department'].str.upper().str.strip()

        # change convert joindate into date 
        df['joinDate'] = pd.to_datetime(df['joinDate'],errors='coerce')

        # find total time spend by emlpoyee in company (tenure)
        current_date = datetime.now()
        df['tenure_year'] = (current_date - df['joinDate']).dt.days // 365

        # drop duplicate
        df = df.drop_duplicates(subset=['name','joinDate'],keep='last')

        remove_duplicate_record = df['employeeID'].count()
        remove_records = total_record - remove_duplicate_record
        logger.info(f'total removed records: {remove_records}')
        logger.info(f'total records after deduplicate : {remove_duplicate_record}')

        # drop null
        transfromed_df = df.dropna(subset=['employeeID','name'])

    except Exception as e:
        logger.error(f'Error during transformation: {e}')
        raise e 
    return transfromed_df 
    logger.info("data transformation finished...")
