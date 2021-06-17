# import packages
import pandas as pd


# import csv file
filename= 'ESurvey.csv'
data = pd.read_csv((filename), low_memory=False)

# print heads and some info on dataframe
print(data.head())
print(data.info())
print(data.shape)

# Count number of responses of each country and the proportion
resp_counts = data['B001'].value_counts()
resp_prop = data['B001'].value_counts(normalize=True)
print(resp_counts, resp_prop)

