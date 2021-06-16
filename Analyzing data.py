# import packages
import pandas as pd

# import csv file
filename = 'ESurvey.csv'
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


# Function that checks for missing values in age column and replaces with mean
print('Number of missing values in the AGE column:')
def check_and_replace():
    print(data['B003_01'].isnull().sum())
    data['B003_01'] = data['B003_01'].fillna(data['B003_01'].mean())
check_and_replace()
print('Number of missing values in the AGE column after the clean up:')
print(data['B003_01'].isnull().sum())

# creates firstwave; secondwave; thirdwave filtering by wave field
firstwave = data.loc[data['wave'] == 1]
secondwave = data.loc[data['wave'] == 2]
thirdwave = data.loc[data['wave'] == 3]

# Merge firstwave with secondwave
firstandsecond = pd.concat([firstwave,secondwave],axis=0)
print (firstandsecond.info())


#Iterate over rows
for index, row in data.iterrows():
     print('The contributor number ', index, '  lives in ', row['B001'])
