# import packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# import csv file
filename= 'ESurvey.csv'
data = pd.read_csv((filename), low_memory=False)
wheredoyoulive = data['B001']

#creates firstwave; secondwave; thirdwave filtering by wave field
firstwave = data.loc[data['wave'] == 1]
secondwave = data.loc[data['wave'] == 2]
thirdwave = data.loc[data['wave'] == 3]

#Seaborn graph 'Country of origin of the contributions' sorted. All waves
# def graphsize():
#     sns.set(rc={"figure.figsize":(12, 5)})
# graphsize()
# sns.countplot(y=wheredoyoulive,  data=data, order = data['B001'].value_counts().index)
# plt.title("Country of origin of the contributions")
# plt.xlabel('n. of contributions')
# plt.ylabel('Country')
# plt.show()

#Seaborn catplot 'where do you live' by wave

sns.catplot(y='B001', col="wave", data=data, order = data['B001'].value_counts().index, kind="count")
plt.show()
