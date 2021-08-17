# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:41:26 2021

@author: Dell
"""
#import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#import the dataset
df=pd.read_csv(r"C:\Users\Dell\Downloads\winequality-red.csv")

#use the dataframe as wine
wine=df
wine

#Data profiling

wine.head()
wine.tail()
type(wine)
len(wine)
wine.shape
wine.ndim
wine.describe
wine.isnull().sum()
wine.duplicated()
wine.info()

#Check the amount of duplicate values

wine.drop_duplicates()
wine2=wine.drop_duplicates()

#Get the Unique values

wine2["pH"].unique()
len(wine2["pH"].unique())

wine3=wine2["quality"].unique()

#find the correlation of indicators 
correlation=wine2.corr()
correlation()

#Plot heatmap
plt.figure(figsize=(20, 17))
matrix = np.triu(wine2.corr())
sns.heatmap(wine2.corr(), annot=True,
            linewidth=.8, mask=matrix, cmap="rocket")


#Classify the quality of wine according to its alcohol content
wine2.groupby("quality")["alcohol"].mean().plot(kind='bar')
plt.show()

#cat plot
sns.catplot(x="quality", y="fixed acidity", data=wine2, kind="box")
sns.catplot(x="quality", y="volatile acidity", data=wine2, kind="box")
sns.catplot(x="quality", y="citric acid", data=wine2, kind="box")
sns.catplot(x="quality", y="residual sugar", data=wine2, kind="box")
sns.catplot(x="quality", y="chlorides", data=wine2, kind="box")
sns.catplot(x="quality", y="density", data=wine2, kind="box")
sns.catplot(x="quality", y="pH", data=wine2, kind="box")
sns.catplot(x="quality", y="sulphates", data=wine2, kind="box")
sns.catplot(x="quality", y="alcohol", data=wine2, kind="box")

acidity_count = wine2["fixed acidity"].value_counts().reset_index()
acidity_count

plt.figure(figsize=(30, 10))
plt.style.use("ggplot")
sns.barplot(x=acidity_count["index"], y=acidity_count["fixed acidity"])
plt.title("TYPE OF ACIDITY WITH QUALITY", fontsize=20)
plt.xlabel("ACIDITY", fontsize=20)
plt.ylabel("COUNT", fontsize=20)
plt.show()

#DISTRIBUTION LIST

plt.style.use("ggplot")
sns.distplot(wine2["pH"]);  # using displot here
plt.title("DISTRIBUTION OF pH FOR DIFFERENT QUALITIES", fontsize=18)
plt.xlabel("pH", fontsize=20)
plt.ylabel("COUNT", fontsize=20)
plt.show()

#VIOLINPLOT---------------

sns.violinplot(x="quality", y="fixed acidity", data=wine2)
sns.violinplot(x="quality", y="pH", data=wine2)
sns.violinplot(x="quality", y="density", data=wine2)
sns.violinplot(x="quality", y="residual sugar", data=wine2)
sns.violinplot(x="quality", y="alcohol", data=wine2)
sns.violinplot(x="quality", y="chlorides", data=wine2)

#histogram---------------------------------------
def draw_histograms(wine2, variables, n_rows, n_cols):
    fig=plt.figure(figsize=(12,10))
    for i, var_name in enumerate(variables):
        ax=fig.add_subplot(n_rows,n_cols,i+1)
        plt.hist(df[var_name],edgecolor='black')
        ax.set_title(var_name.upper())
    fig.tight_layout()
    plt.show()

draw_histograms(wine2, wine2.columns, 4, 3)

#BOXPLOT-------------------------

plt.figure(figsize=(15,10))

for i,var_name in enumerate(list(wine2.columns)):
    plt.subplot(4,3,i+1)
    sns.boxplot(x=var_name, data=wine2)
    plt.title(var_name.upper())
    plt.xlabel(None)
    plt.ylabel(None)
    
plt.tight_layout()
plt.show()

#stripplots--------

sns.stripplot(x="quality", y="fixed acidity", data=wine2)
sns.stripplot(x="quality", y="pH", data=wine2)
sns.stripplot(x="quality", y="density", data=wine2)
sns.stripplot(x="quality", y="residual sugar", data=wine2)
sns.stripplot(x="quality", y="alcohol", data=wine2)
sns.stripplot(x="quality", y="chlorides", data=wine2)
