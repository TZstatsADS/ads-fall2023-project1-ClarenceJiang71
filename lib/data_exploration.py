#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

def data_info_present(df):
    print(f"There are {df.shape[0]} rows and {df.shape[1]} features")
    print("-" * 10)
    print(f"Check what features are there and the data type")
    print(df.dtypes)
    print("-" * 10)
    print("Check how many uniques value for each column")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()} unique values")
    print("-"*10)
    print("Check for missing values:")
    print(df.isnull().sum())
    print("-"*10)
    print("Check if there is any duplicated row")
    print(f"Number of duplicate rows: {df.duplicated().sum()}")
    
def feature_reduction(df):
    df_proc = df.drop(columns = ["original_hm", "modified", "ground_truth_category"])
    return df_proc

def bar_chart_visualization(df, category):
    category_counts = df[category].value_counts()

    # Plot the counts
    category_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Category Counts')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.xticks(rotation=45)  # Optional: rotate x-labels if they overlap
    plt.show()
    

# In[ ]:




