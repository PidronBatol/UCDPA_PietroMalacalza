# import packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# import csv file
filename = 'ESurvey.csv'
data = pd.read_csv((filename), low_memory=False)
wheredoyoulive = data['B001']

# creates firstwave; secondwave; thirdwave filtering by wave field
firstwave = data.loc[data['wave'] == 1]
secondwave = data.loc[data['wave'] == 2]
thirdwave = data.loc[data['wave'] == 3]

# Age of the respondents
binsr = np.arange(0, 101, 20)
data[['B003_01']].plot(kind='hist', bins=binsr, rwidth=0.8, legend=False, title='Age of the respondents')
plt.show()

# Happiness and Satisfaction first wave on same graph
plt.hist(firstwave[['C002_01']], color='red', bins=range(0,12), alpha=0.8)
plt.hist(firstwave[['C001_01']], color='blue', bins=range(0,12), alpha=0.8)
plt.title('Happiness and Satis first wave')
plt.xlabel('Happiness and Satis')
plt.ylabel('count')
plt.show()

# Evolution of Life Satisfaction across survey waves
ax = data.hist(column='C001_01', by='wave', bins=10, grid=False, figsize=(8,10), layout=(3,1), sharex=True, zorder=2, rwidth=0.9)
for i,x in enumerate(ax):
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)
    x.set_xlabel("Evolution of Life Satisfaction across waves", labelpad=20, weight='bold', size=12)
    if i == 1:
        x.set_ylabel("Contributions", labelpad=50, weight='bold', size=12)
plt.show()

# Life satisfaction by gender
ax = data.hist(column='C001_01', by='B002', bins=10, grid=False, figsize=(8,10), layout=(3,1), sharex=True, zorder=2, rwidth=0.9)
for i,x in enumerate(ax):
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)
    x.set_xlabel("Life Satisfaction by gender", labelpad=20, weight='bold', size=12)
    if i == 1:
        x.set_ylabel("Contributions", labelpad=50, weight='bold', size=12)
plt.show()

# Replace missing values in C007_01; C007_02; C007_03; C007_04 and C007_05 ('Trust in institutions' fields) with mean
data['C007_01'] = data['C007_01'].fillna(data['C007_01'].mean())
data['C007_02'] = data['C007_02'].fillna(data['C007_02'].mean())
data['C007_03'] = data['C007_03'].fillna(data['C007_03'].mean())
data['C007_04'] = data['C007_04'].fillna(data['C007_04'].mean())
data['C007_05'] = data['C007_05'].fillna(data['C007_05'].mean())

# Create calculated field ('Trust in institutions')
data['trust'] = data.C007_01 + data.C007_02 + data.C007_03 + data.C007_03 + data.C007_04 + data.C007_05

# Replace missing values in C005_01, C005_02, C005_03, C005_04, C005_05 (WHO-5 index) with mean
data['C005_01'] = data['C005_01'].fillna(data['C005_01'].mean())
data['C005_02'] = data['C005_02'].fillna(data['C005_02'].mean())
data['C005_03'] = data['C005_03'].fillna(data['C005_03'].mean())
data['C005_04'] = data['C005_04'].fillna(data['C005_04'].mean())
data['C005_05'] = data['C005_05'].fillna(data['C005_05'].mean())

# Create calculated field ('WHO-5 Well-Being Index')
data['who5'] = data.C005_01 + data.C005_02 + data.C005_03 + data.C005_03 + data.C005_04 + data.C005_05



# Scatter trust vs age
# Sample 5000 lines to avoid overplotting
data_sample = data.sample(5000)
plt.plot('B003_01', 'trust', "", data=data_sample, linestyle='', marker='o', markersize=5, alpha=0.09,  color="purple")
plt.xlabel('Age')
plt.ylabel('Trust')
plt.title('Trust in institutions vs Age', loc='left')
plt.show()

# Scatter trust vs wh05
# Sample 5000 lines to avoid overplotting
data_sample = data.sample(5000)
plt.plot('who5', 'trust', "", data=data_sample, linestyle='', marker='o', markersize=10, alpha=0.09,  color="purple")
plt.xlabel('who5')
plt.ylabel('Trust')
plt.title('Trust in institutions vs WHO5 well being index', loc='left')
plt.show()


