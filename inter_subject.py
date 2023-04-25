import pandas as pd

from utils import *


df = import_csv()

# Getting Gender and Age
gender = df['gender']
age = df['age']
df = df.drop(['gender', 'age'], axis = 1)

experience = df['experience']
df['experience'] = return_exp(experience)


df_experience = df[df['experience'] == 1].reset_index(drop = True)
df_unexperience = df[df['experience'] == 0].reset_index(drop = True)

matrices_experience = create_matrices(df_experience)
matrices_unexperience = create_matrices(df_unexperience)
matrices = create_matrices(df)


cronbach_experience = cronbach(matrices_experience)
cronbach_unexperience = cronbach(matrices_unexperience)
cronbach_all = cronbach(matrices)

df_experience = df[df['experience'] == 1].drop(['experience'], axis = 1).reset_index(drop = True)
df_unexperience = df[df['experience'] == 0].drop(['experience'], axis = 1).reset_index(drop = True)


dfs_experience = split_df(df_experience)
dfs_unexperience = split_df(df_unexperience)
df = df.drop(['experience'], axis = 1).reset_index(drop = True)





order = ["Warmth", "Acousticness", "Colourfulness", "Fullness", "Energy"]




experienced_users = split_subject(df_experience)
unexperienced_users = split_subject(df_unexperience)
users = split_subject(df)

experienced_corr = return_corr_matrix(experienced_users)
unexperienced_corr = return_corr_matrix(unexperienced_users)
corr = return_corr_matrix(users)

experienced_corr_mean = np.mean(experienced_corr, axis = 0)
unexperienced_corr_mean = np.mean(unexperienced_corr, axis = 0)
corr_mean = np.mean(corr, axis = 0)


print("Experienced:")
print(experienced_corr_mean)
print("Unexperienced:")
print(unexperienced_corr_mean)
print("All:")
print(corr_mean)





print("\n\n\nCRONBACH ALPHA VALUES")

print("Cronbach Experienced:")
print(cronbach_experience)
print("Cronbach Unexperienced:")
print(cronbach_unexperience)
print("Cronbach All:")
print(cronbach_all)