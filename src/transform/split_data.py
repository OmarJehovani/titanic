import pandas as pd 
from typing import Tuple
from sklearn.model_selection import train_test_split 

SEED_SPLIT = 404
DATASETS_DIR = 'datasets/' 
TRAIN_DATA_FILE = DATASETS_DIR + 'train.csv'
TEST_DATA_FILE  = DATASETS_DIR + 'test.csv'
RETRIEVED_DATA = 'raw-data.csv' 

class SplitData:  
    def __init__(self) -> None:
        pass

    def split_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        df = pd.read_csv(DATASETS_DIR + RETRIEVED_DATA)

        X_train, X_test, y_train, y_test = train_test_split(
                                                            df.drop(TARGET, axis=1),
                                                            df[TARGET],
                                                            test_size=0.2,
                                                            random_state=404
                                                    )

        X_train.to_csv(TRAIN_DATA_FILE, index=False)
        X_test.to_csv(TEST_DATA_FILE, index=False)
        y_test.to_csv('y_test.csv', index=False)
        
        return self.X_train, self.X_test, self.y_test