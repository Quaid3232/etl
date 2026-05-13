import pandas as pd
from loguru import logger

def extraction(path):
    df = None
    logger.info("data extraction starting...")
    try:
        if path.endswith(".json"):
            df=pd.read_json(path)
            logger.info(f'file format is json')
        elif path.endswith('.csv'):
            df = pd.read_csv(path)
            logger.info(f'file format is csv')
        elif path.endswith('.parquet'):
            df = pd.read_parquet(path)
            logger.info(f'file format is parquet')
        else:
            logger.error(f"file format is inviled: {path}")
            return None
    except Exception as e:
        logger.error(f'error: {e}')
    return df
    logger.info("data extraction finished...")