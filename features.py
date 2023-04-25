from utils import *
# This is the sequence of the files. 
df = import_csv()

# Getting Gender and Age
gender = df['gender']
age = df['age']
df = df.drop(['gender', 'age'], axis = 1)

experience = df['experience']
df['experience'] = return_exp(experience)


df_experience = df[df['experience'] == 1].drop(['experience'], axis = 1)
df_unexperience = df[df['experience'] == 0].drop(['experience'], axis = 1)

dfs_experience = split_df(df_experience)
dfs_unexperience = split_df(df_unexperience)
df = df.drop(['experience'], axis = 1)
mean_experience = np.array([j.mean().values for j in dfs_experience])
mean_unexperience = np.array([j.mean().values for j in dfs_unexperience])
mean = np.array([j.mean().values for j in split_df(df)])


feature_df = pd.read_csv('./features.csv')
feature_df = feature_df.drop(['File Name'], axis = 1)
feature_df.head()
features = feature_df.keys()

order = ["Warmth", "Acousticness", "Colourfulness", "Fullness", "Energy"]

feature_timbre_corr_experience = return_feature_timbre_corr(feature_df, mean_experience, features, order)
feature_timbre_corr_unexperience = return_feature_timbre_corr(feature_df, mean_unexperience, features, order)
feature_timbre_corr = return_feature_timbre_corr(feature_df, mean, features, order)

feature_timbre_corr_experience = dict_sort(feature_timbre_corr_experience)
feature_timbre_corr_unexperience = dict_sort(feature_timbre_corr_unexperience)
feature_timbre_corr = dict_sort(feature_timbre_corr)

pd.DataFrame(feature_timbre_corr_experience, index=[0]).to_csv("feature_timbre_corr_experience.csv")
pd.DataFrame(feature_timbre_corr_unexperience, index=[0]).to_csv("feature_timbre_corr_unexperience.csv")
pd.DataFrame(feature_timbre_corr, index=[0]).to_csv("feature_timbre_corr.csv")
