import matplotlib as mp
import scipy as sc
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from scipy.stats import linregress
import json
# from census import Census

# Import gmaps
import matplotlib.ticker as mtick
import seaborn as sns

print("************************************************")

# Census and gmaps API keys
# from config import (api_key, gkey)
# c = Census("a86ea43f22404e5a382b5659408275feb9034e6d", year=2018)
# gmaps.configure(api_key = gkey)

# Import Racial Data .csv
csv_path = "/linear_regression/some_data.csv"

# Import the .csv as a dataframe and treat the first column as the ID column
race_df = pd.read_csv(csv_path, index_col=0)

# Display the observations
race_df.head()  # first 5
print(race_df)  # more

# Data Management

# dropna: Drop missing values.
# thresh: keep only the rows with 9 non-NA values.
race_df = race_df.dropna(thresh=9)

# subset: define in which columns to look for missing values
race_df = race_df.dropna(subset=['Cases_White'])
race_df = race_df.dropna(subset=['Cases_Black'])

# Subset the dataframe to a specific date
# race_df = race_df[(race_df['Date'] == 20200715)]

# Display remaining data
print(race_df)
print("************************************************")

t_stat, p_value = stats.ttest_ind(race_df['Cases_White'], race_df['Cases_Black'], equal_var=True)
print(t_stat)
print(p_value)
print("end of file")

# Simple Linear Regression with linregress

# x = list(range(0,3))
# y = race_df['Cases_Total']
# slope, intercept, r_value, p_value, std_err = linregress(x,y)
# print("slope: %f    intercept: %f" % (slope, intercept))
# print("R-squared: %f" % r_value**2)

# plt.plot(x,y,'o', label='original data')
# plt.plot(x, intercept + slope*np.asarray(x), 'r', label='fitted line')
# plt.legend()
# plt.show()


## ANOVA
# mydata = pd.read_csv("PlantGrowth.csv")\

# Create a boxplot
# fig = plt.figure(figsize=(12,8))
# sns.boxplot(x = mydata['group'], y = mydata['weight'])
# plt.show()


# ctrl = mydata['weight'][mydata.group == 'ctrl']
# print("ctrl: ")
# print(ctrl)

# grps = pd.unique(mydata.group.values)
# print("grps: ")
# print(grps)

# d_data = {grp:mydata['weight'][mydata.group == grp] for grp in grps}
# print("d_data: ")
# print(d_data)

# k = len(pd.unique(mydata.group)) # number of conditions
# print("k (number of conditions)")
# print(k)

# N = len(mydata.values) # conditions times participants
# print("N (number of samples or trials)")
# print(N)

# n = mydata.groupby('group').size()[0] # participants in each condition
# print("n (participants in each condition)")
# print(n)
