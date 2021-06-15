# import packages
import pandas as pd

# import csv file
filename= 'ESurvey.csv'
data = pd.read_csv((filename), low_memory=False)

# Group summary of happiness (mean) by country and gender
happynessbycountry = data.groupby(['B001', 'B002'])['C002_01'].mean().round(2)
pd.set_option('display.max_rows', None)
print('Happiness by country (scale of 1 to 10) and gender')
print(happynessbycountry)

# Happiest country (ascending order)
happiestcountry = data.groupby(['B001'])['C002_01'].mean().sort_values(ascending=False).round(2)

print('Country happiness during Covid time')
print(happiestcountry)