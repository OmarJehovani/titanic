import re 
import pandas as pd
import numpy as np
from typing import Tuple 

DATASETS_DIR = 'datasets/' 
#URL = 'https://www.openml.org/data/get_csv/16826755/phpMYEkMl'
DROP_COLS = ['boat','body','home.dest','ticket','name']
RETRIEVED_DATA = 'raw-data.csv'

SEED_SPLIT = 404
TRAIN_DATA_FILE = DATASETS_DIR + 'train.csv'
TEST_DATA_FILE  = DATASETS_DIR + 'test.csv'

TARGET = 'survived'
FEATURES = ['pclass','sex','age','sibsp','parch','fare','cabin','embarked','title']
NUMERICAL_VARS = ['pclass','age','sibsp','parch','fare']
CATEGORICAL_VARS = ['sex','cabin','embarked','title']

NUMERICAL_VARS_WITH_NA = ['age','fare']
CATEGORICAL_VARS_WITH_NA = ['cabin','embarked']
NUMERICAL_NA_NOT_ALLOWED = [var for var in NUMERICAL_VARS if var not in NUMERICAL_VARS_WITH_NA]
CATEGORICAL_NA_NOT_ALLOWED = [var for var in CATEGORICAL_VARS if var not in CATEGORICAL_VARS_WITH_NA]

SEED_MODEL = 404

class TitanicLoadData: 

    def __init__(self) -> None:
        pass

    def data_retrieval(path):
        
        # Loading data from specific url
        data = pd.read_csv(path)
        
        # Uncovering missing data
        data.replace('?', np.nan, inplace=True)
        data['age'] = data['age'].astype('float')
        data['fare'] = data['fare'].astype('float')
        
        # helper function 1
        def get_first_cabin(row):
            try:
                return row.split()[0]
            except:
                return np.nan
        
        # helper function 2
        def get_title(passenger):
            line = passenger
            if re.search('Mrs', line):
                return 'Mrs'
            elif re.search('Mr', line):
                return 'Mr'
            elif re.search('Miss', line):
                return 'Miss'
            elif re.search('Master', line):
                return 'Master'
            else:
                return 'Other'
        
        # Keep only one cabin | Extract the title from 'name'
        data['cabin'] = data['cabin'].apply(get_first_cabin)
        data['title'] = data['name'].apply(get_title)
        
        # Droping irrelevant columns
        data.drop(DROP_COLS, 1, inplace=True)
        
        data.to_csv(DATASETS_DIR + RETRIEVED_DATA, index=False)
        
        return print('Data stored in {}'.format(DATASETS_DIR + RETRIEVED_DATA))