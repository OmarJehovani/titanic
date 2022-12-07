import os

import ssl
import certifi
from urllib.request import urlopen

request = "https://www.openml.org/data/get_csv/16826755/phpMYEkMl"
URL = urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))

BASE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
ROOT_DIR = os.path.realpath(os.path.join(BASE_DIR, ".."))
PATH_MODEL = os.path.realpath(os.path.join(ROOT_DIR, "titanic_train/models", "model.sav"))
LOG_DIR = os.path.realpath(os.path.join(BASE_DIR, "logs")) 

SEED_SPLIT = 404
SEED_MODEL = 404

#MODEL_NAME = os.path.realpath(os.path.join(BASE_DIR, "titanic_train/src/titanic_train/models", "model.sav"))
TARGET = "survived"
FEATURES = [
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "cabin",
    "embarked",
    "title",
]
NUMERICAL_VARS = ["pclass", "age", "sibsp", "parch", "fare"]
CATEGORICAL_VARS = ["sex", "cabin", "embarked", "title"]
DROP_COLS = ["boat", "body", "ticket", "name"]
TARGET = "survived"