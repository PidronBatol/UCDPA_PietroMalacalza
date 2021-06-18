# import packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# import csv file
filename= 'ESurvey.csv'
data = pd.read_csv((filename), low_memory=False)
wheredoyoulive = data['B001']

#creates firstwave; secondwave; thirdwave filtering by wave field
firstwave = data.loc[data['wave'] == 1]
secondwave = data.loc[data['wave'] == 2]
thirdwave = data.loc[data['wave'] == 3]

#G4 Seaborn graph 'Country of origin of the contributions' sorted. All waves
def graphsize():
    sns.set(rc={"figure.figsize":(12, 5)})
graphsize()
sns.countplot(y=wheredoyoulive,  data=data, order = data['B001'].value_counts().index)
plt.title("Country of origin of the contributions")
plt.xlabel('n. of contributions')
plt.ylabel('Country')
plt.show()

#G5 Seaborn catplot 'where do you live' by wave
sns.catplot(y='B001', col="wave", data=data, order = data['B001'].value_counts().index, kind="count")
plt.show()

#G6 Seaborn hexbin plot: life satisfaction and happiness
joint_kws=dict(gridsize=7) #the higher, the smaller the bins
sns.jointplot(x="C002_01", y="C001_01", data=data, kind="hex", space=0, joint_kws=joint_kws, marginal_ticks=True, marginal_kws=dict(bins=10))
plt.xlabel('Happiness')
plt.ylabel('Life Satisfaction')
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
# G7 Seaborn hexbin plot: life satisfaction and happiness
joint_kws=dict(gridsize=10) #the higher, the smaller the bins
sns.jointplot(x="who5", y="trust", data=data, kind="hex", space=0, joint_kws=joint_kws, marginal_ticks=True, marginal_kws=dict(bins=10))
plt.xlabel('WHO5 Well-Being Index ')
plt.ylabel('Trust')
plt.show()