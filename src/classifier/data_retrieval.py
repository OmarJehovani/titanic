from load.load_data import TitanicLoadData
import joblib
import logging
from pathlib import Path
import sys


import numpy as np

class TitanicClassifier:
    def __init__(self):
        load = TitanicLoadData()
