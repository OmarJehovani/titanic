import re
import numpy as np


def get_first_cabin(row):
    """
    get cabin number
    Args:
        row (text): row from dataframe
    """

    try: 
        return row.split()[0]
    except AttributeError:
        return np.nan

def get_title(name):
    """
    Separate and get the title from name

    Args:
        name (text): name register from dataframe 

    Returns:
        title: according to the string found within the name
    """
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