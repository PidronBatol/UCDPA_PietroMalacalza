# import packages
import numpy as np
import pandas as pd

# import csv file
filename = 'ESurvey.csv'
data = pd.read_csv((filename), low_memory=False)

# Function that checks for missing values in age column and replaces with mean
# print('Number of missing values in the AGE column:')
# def check_and_replace():
#     print(data['B003_01'].isnull().sum())
#     data['B003_01'] = data['B003_01'].fillna(data['B003_01'].mean())
# check_and_replace()
# print('Number of missing values in the AGE column after the clean up:')
# print(data['B003_01'].isnull().sum())

# Convert dataframe into NumPy array and print shape (138629 lines and 440 columns) and type; print the ninth column (country)
# arr = data.to_numpy()
# print(arr.shape)
# print(type(arr))
# country = arr[:, 8]
# print(country)

# Convert dataframe into dictionary
dictio = data.to_dict()
# print(dictio)
print('Total lenght of the dictionary: ')
print(len(dictio))
