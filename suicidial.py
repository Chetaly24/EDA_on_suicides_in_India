**Import Libraries**

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Reading the dataset
df = pd.read_csv('/kaggle/input/suicides-in-india/Suicides in India 2001-2012.csv')
df

#Preprocessing the data
df.isna().sum()
df.drop_duplicates()
df.State.unique()
df = df.drop(df[(df.State == 'Total (Uts)') | (df.State == 'Total (All India)') | 
               (df.State == 'Total (States)')].index)
df.State.unique()
df.Year.unique()
df.Type.unique()
df[df['Type']=='Bankruptcy or Sudden change in Economic']
df['Type'] = df['Type'].replace(['Bankruptcy or Sudden change in Economic'],'Bankruptcy or Sudden change in Economic Status')
df=df.drop(df[(df.Type =='By Other means')|(df.Type=='Other Causes (Please Specity)')| (df.Type=='Others (Please Specify)')|(df.Type=='Causes Not known')].index)
df = df.drop(df[df['Total'] == 0].index)
df.Gender.unique()
df[df['Age_group']=='0-100+']
df_wa = df[df['Age_group']!='0-100+']
df_wa

#Analyzing Data 
#State wise 

plt.figure(figsize=(16,8))
df_st = df.groupby('State').sum().Total.sort_values(ascending=False)
sns.barplot(y=df_st.index,x=df_st.values,orient='h')
plt.ylabel('State')
plt.title('Suicide stat State-wise')

#Age group wise

plt.figure(figsize=(14,8))
df_ag = df_wa.groupby('Age_group').sum().Total
sns.barplot(x=df_ag.index,y=df_ag.values)
plt.xlabel('Age Group')
plt.title('Suicides per Age Group')

#Max suicides are in age 15 to 44

plt.figure(figsize=(14,8))
sns.barplot(x=df_wa.Age_group,y=df_wa.Total,hue=df.Gender)
plt.xlabel('Age Group')
plt.title('Suicides per Age Group')

#Year Wise

plt.figure(figsize=(14,8))
df_yr = df.groupby('Year').sum().Total
sns.lineplot(x=df_yr.index,y=df_yr.values,marker='o',markerfacecolor='k')
plt.xlabel('Year')
plt.title('Suicides per Year')

#Type Wise

plt.figure(figsize=(14,8))
df_tc = df.groupby('Type_code').sum().Total
df_tc = df_tc.sort_values(ascending=False)
sns.barplot(x=df_tc.index,y=df_tc.values)
plt.xlabel('State')
plt.title('Suicide vs State')

#Social Status

df_ss=df[df['Type_code']=='Social_Status']
df_ss_tp = df_ss.groupby('Type').sum().Total
df_ss_tp = df_ss_tp.sort_values(ascending=False)
plt.figure(figsize=(14,8))
sns.barplot(x=df_ss_tp.index,y=df_ss_tp.values)
plt.xlabel('Type of Social Status')
plt.title('Suicide vs Social Status')

#Professional profile
df_pp=df[df['Type_code']=='Professional_Profile']
df_pp_tp = df_pp.groupby('Type').sum().Total
df_pp_tp = df_pp_tp.sort_values(ascending=True)
plt.figure(figsize=(12,6))
sns.barplot(y=df_pp_tp.index,x=df_pp_tp.values,orient='h')
plt.xlabel('Professional Profile')
plt.title('Suicide vs Professional Profile')

#Now Top 5 states with most cases of housewives suicide.

df_pp_housewife = df_pp[df_pp['Type']=='House Wife']
df_pp_housewife_s=df_pp_housewife.groupby('State').sum().Total.sort_values(ascending=False)
df_pp_housewife_s[:5]

#Top 5 states with most cases of farmer suicide.

df_pp_farmer = df_pp[df_pp['Type']=='Farming/Agriculture Activity']
df_pp_farmer_s=df_pp_farmer.groupby('State').sum().Total.sort_values(ascending=False)
df_pp_farmer_s[:5]

#Education Status
df_es=df[df['Type_code']=='Education_Status']
df_es_tp = df_es.groupby('Type').sum().Total
df_es_tp = df_es_tp.sort_values(ascending=True)
plt.figure(figsize=(12,6))
sns.barplot(y=df_es_tp.index,x=df_es_tp.values,orient='h')
plt.xlabel('Education Status')
plt.title('Suicide vs Education Status')

#Causes
df_cs=df[df['Type_code']=='Causes']
df_cs_tp = df_cs.groupby('Type').sum().Total
df_cs_tp = df_cs_tp.sort_values(ascending=True)
plt.figure(figsize=(15,12))
sns.barplot(y=df_cs_tp.index,x=df_cs_tp.values,orient='h')
plt.xlabel('Education Status')
plt.title('Suicide vs Education Status')

#Means Adopted
df_ma=df[df['Type_code']=='Means_adopted']
df_ma_tp = df_ma.groupby('Type').sum().Total
df_ma_tp = df_ma_tp.sort_values(ascending=True)
plt.figure(figsize=(15,6))
sns.barplot(y=df_ma_tp.index,x=df_ma_tp.values,orient='h')
plt.xlabel('Education Status')
plt.title('Suicide vs Education Status')
