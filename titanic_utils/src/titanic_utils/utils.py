import re
import numpy as np


def get_first_cabin(row):
    """
    Args:
        row (_type_): _description_
    """

    try: 
        return row.split()[0]
    except AttributeError:
        return np.nan

def get_title(name):
    if re.search("Mrs", name):
        return "Mrs"
    elif re.search("Mr", name):
        return "Mr"
    elif re.search("Miss", name):
        return "Miss"   
    elif re.search("Master", name):
        return "Master"   
    else:
        return "Other"