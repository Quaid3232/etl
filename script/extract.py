import pandas as pd
from loguru import logger

def extraction(path):
    df = None
    try:
        if path.endswith(".json"):
            df=pd.read_json(path)
        elif path.endswith('.csv'):
            df = pd.read_csv(path)
        elif path.endswith('.parquet'):
            df = pd.read_parquet(path)
        else:
            logger.error(f"file format is inviled: {path}")
            return None
    except Exception as e:
        logger.error(f'error: {e}')
    return df