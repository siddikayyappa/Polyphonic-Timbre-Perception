from utils import *


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

mean_experience = np.array([j.mean().values for j in dfs_experience])
mean_unexperience = np.array([j.mean().values for j in dfs_unexperience])

# print(mean_experience)

corr_ar = np.zeros((len(mean_experience[0]), len(mean_experience[0])))
for i in range(len(mean_experience[0])):
    for j in range(i, len(mean_experience[0])):
        # print(i, j, correlation(mean_experience[:, i], mean_experience[:, j]))
        corr_ar[i][j] = correlation(mean_experience[:, i], mean_experience[:, j])


bin_mean_exp = convert_bool(mean_experience)
bin_mean_unexp = convert_bool(mean_unexperience)