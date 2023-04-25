import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from scipy.stats import kendalltau
import pingouin as pg

def create_dict():
    dict_1 = dict()
    for i in range(20):
        if(i != 0):
            dict_1["On a scale of 1-10 how warm is the song? (10 corresponds to very warm)."+str(i)] = "q"+str(i)+"_warm"
            dict_1["On a scale of 1-10 how acoustic is the song? (10 corresponds to very acoustic)."+str(i)] = "q"+str(i)+"_acoustic"
            dict_1["On a scale of 1-10 how colourful is the song? (10 corresponds to very colourful)."+str(i)] = "q"+str(i)+"_colourful"
            dict_1["On a scale of 1-10 how full is the song? (10 corresponds to very full)."+str(i)] = "q"+str(i)+"_full"
            dict_1["On a scale of 1-10 how Energetic is the song? (10 corresponds to very Energetic)."+str(i)] = "q"+str(i)+"_energy"
        else:
            dict_1["On a scale of 1-10 how warm is the song? (10 corresponds to very warm)"] = "q"+str(i)+"_warm"
            dict_1["On a scale of 1-10 how acoustic is the song? (10 corresponds to very acoustic)"] = "q"+str(i)+"_acoustic"
            dict_1["On a scale of 1-10 how colourful is the song? (10 corresponds to very colourful)"] = "q"+str(i)+"_colourful"
            dict_1["On a scale of 1-10 how full is the song? (10 corresponds to very full)"] = "q"+str(i)+"_full"
            dict_1["On a scale of 1-10 how Energetic is the song? (10 corresponds to very Energetic)"] = "q"+str(i)+"_energy"
    return dict_1


def import_csv():
    """
    Imports the csv file and returns a pandas dataframe
    """
    df = pd.read_csv('./data.csv')
    df = df.drop(['Timestamp'], axis = 1)
    df = df.rename(columns={"Enter the amount of experience you have in music (Instruments or Vocals)":"experience", "Please enter your age in years":"age", "Please select your gender":"gender"})
    df = df.rename(columns=create_dict())
    return df

def return_exp(experience):
    list_1 = []
    for i in range(len(experience)):
        if(experience[i] == "No Experience"):
            list_1 += [0]
        else:
            list_1 += [1]
    return list_1

def split_df(df):
    dfs = np.array_split(df, len(df.columns)//5, axis = 1)
    return dfs

def convert_bool(mean_array):
    for i in range(len(mean_array)):
        for j in range(len(mean_array[i])):
            if(mean_array[i][j] > 5):
                mean_array[i][j] = 1
            else:
                mean_array[i][j] = 0
    return mean_array


def correlation(a, b):
    """
    Returns the correlation between two arrays
    """
    a = a - np.mean(a)
    b = b - np.mean(b)
    return np.sum(a*b) /( np.sqrt(np.sum(a*a) * np.sum(b*b)))



def spearman_corr(x, y):
    # Use scipy's spearmanr function to calculate Spearman's rho
    rho, _ = spearmanr(x, y)
    
    return rho



def kendall_corr(x, y):
    # Use scipy's kendalltau function to calculate Kendall's tau
    tau, _ = kendalltau(x, y)
    
    return tau



def split_subject(df):
    users = []
    for i in range(len(df)):
        df_1 = df.loc[i].to_frame().T
        temp = split_df(df_1)
        for i in range(len(temp)):
            temp[i] = temp[i].values
        temp = np.array(temp)
        users += [temp.reshape(-1, 5)]
    return users

def correlation_users(user_1, user_2):
    corr = []
    for i in range(len(user_1[0])):
        corr += [(correlation(user_1[:, i], user_2[:, i]))]
    corr = np.array(corr)
    return corr

def return_corr_matrix(users):
    list_1 = []
    for i in range(len(users)):
        for j in range(i, len(users)):
            list_1 += [(correlation_users(users[i], users[j]))]
    list_1 = np.array(list_1)
    return list_1



def create_keys(character):
    list_1 = []
    for i in range(20):
        list_1 += ["q"+str(i)+"_"+character]
    return list_1

characters = ["warm", "acoustic", "colourful", "full", "energy"]

def create_matrices(df):
    matrices = dict()

    for i in range(len(characters)):
        keys = create_keys(characters[i])
        matrices[characters[i]] = df[keys]
    return matrices

def cronbach(matrix):
    dict_1 = dict()
    key_list = list(matrix.keys())
    for i in range(len(key_list)):
        dict_1[key_list[i]] = pg.cronbach_alpha(matrix[key_list[i]])[0]
    return dict_1

def return_feature_timbre_corr(feature_df, mean_timbre, features, order):
    dict_1 = dict()
    for i in range(len(mean_timbre[0])):
        for j in range(len(features)):
            try:
                dict_1[str(features[j])+"_"+str(order[i])] = correlation(mean_timbre[:, i], feature_df[features[j]].values)
            except:
                print(features[j], order[i])
                print(mean_timbre[:, i], feature_df[features[j]].values)
                print("\n\n\n")
    return dict_1


def dict_sort(dict_1):
    keys = list(dict_1.keys())
    values = list(dict_1.values())
    sorted_values = np.argsort(values)
    sorted_dict = {keys[i]:values[i] for i in sorted_values}
    return sorted_dict
