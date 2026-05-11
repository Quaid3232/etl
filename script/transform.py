import pandas as pd
from loguru import logger
from datetime import datetime
# from script.extract import extraction
from extract import extraction

# def transformat (df):
path = r'C:\Users\intel computer\Documents\Learning Git\data\raw\employee.csv'
df = pd.read_csv(path)

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
df = df.dropna(subset=['employeeID','joinDate'])

