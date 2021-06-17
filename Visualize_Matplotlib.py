# import packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# import csv file
filename = 'ESurvey.csv'
data = pd.read_csv((filename), parse_dates=['STARTED'], index_col='STARTED', low_memory=False)
wheredoyoulive = data['B001']

# creates firstwave; secondwave; thirdwave filtering by wave field
firstwave = data.loc[data['wave'] == 1]
secondwave = data.loc[data['wave'] == 2]
thirdwave = data.loc[data['wave'] == 3]

# Age of the respondents
# binsr = np.arange(0, 101, 20)
# data[['B003_01']].plot(kind='hist', bins=binsr, rwidth=0.8, legend=False, title='Age of the respondents')
# plt.show()

# Happiness and Satisfaction first wave on same graph
# plt.hist(firstwave[['C002_01']], color='red', bins=range(0,12), alpha=0.8)
# plt.hist(firstwave[['C001_01']], color='blue', bins=range(0,12), alpha=0.8)
# plt.title('Happiness and Satis first wave')
# plt.xlabel('Happiness and Satis')
# plt.ylabel('count')
# plt.show()

# Evolution of Life Satisfaction across survey waves
ax = data.hist(column='C001_01', by='wave', bins=10, grid=False, figsize=(8,10), layout=(3,1), sharex=True, zorder=2, rwidth=0.9)
for i,x in enumerate(ax):

    # Switch off ticks
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

    # Draw horizontal axis lines
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    # Set x-axis label
    x.set_xlabel("Evolution of Life Satisfaction across waves", labelpad=20, weight='bold', size=12)

    # Set y-axis label
    if i == 1:
        x.set_ylabel("Contributions", labelpad=50, weight='bold', size=12)

plt.show()