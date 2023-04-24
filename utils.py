import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def import_csv():
    """
    Imports the csv file and returns a pandas dataframe
    """
    df = pd.read_csv('./data.csv')
    return df