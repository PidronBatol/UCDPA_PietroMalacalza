# import packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# import csv file
filename= 'ESurvey.csv'
data = pd.read_csv((filename), low_memory=False)
wheredoyoulive = data['B001']

# creates firstwave; secondwave; thirdwave filtering by wave field
firstwave = data.loc[data['wave'] == 1]
secondwave = data.loc[data['wave'] == 2]
thirdwave = data.loc[data['wave'] == 3]

# Age of the respondants
binsr = np.arange(0, 101, 20)

data[['B003_01']].plot(kind='hist', bins=binsr, rwidth=0.8, legend=False, title='Age of the repondents')
plt.show()
