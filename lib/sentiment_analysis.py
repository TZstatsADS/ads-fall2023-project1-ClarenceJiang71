#!/usr/bin/env python
# coding: utf-8

# In[2]:
import subprocess

def run_command(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    
    if process.returncode != 0:
        print(f"Failed to execute command: {cmd}")
        print(err.decode())
    else:
        print(out.decode())

# Upgrade pip
run_command("python3 -m pip install --upgrade pip")

# Install NRCLex
run_command("python3 -m pip install NRCLex")

# Install textblob 
run_command("python3 -m pip install textblob")

# Download corpora 
run_command("python3 -m textblob.download_corpora")

run_command("python3 -m pip install seaborn")
# run_command("python3 -m pip install matplotlib")



import nrclex 
from nrclex import NRCLex
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from ast import literal_eval

def process_text(df):
    nltk.download('punkt')
    nltk.download('stopwords')
    result = []
#     emotion = []
    
    joy_values = [0] * df.shape[0]
    positive_values = [0] * df.shape[0]
    trust_values = [0] * df.shape[0]
    anticipation_values = [0] * df.shape[0] 
    
    for index, row in df.iterrows():
        sentence = row["cleaned_hm"]
        emotion_values = NRCLex(sentence).top_emotions
        for emotion, value in emotion_values:
            if emotion == 'joy':
                joy_values[index] = value
            elif emotion == 'anticipation':
                anticipation_values[index] = value
            elif emotion == 'trust':
                trust_values[index] = value
            elif emotion == 'positive':
                positive_values[index] = value
        
#         emotion.append(NRCLex(sentence).top_emotions[0][0])
        words = word_tokenize(sentence)
        filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
        happy_words = [word for word in filtered_words if NRCLex(word).top_emotions[0][0] in {"anticipation", "trust", "joy", "positive"}]
        result.append(happy_words)
        
    df["happy_words"] = result
    df["joy_values"] = joy_values
    df["positive_values"] = positive_values
    df["trust_values"] = trust_values
    df["anticipation_values"] = anticipation_values
    
#     df["emotion"] = emotion
    
    df["emotion"] = df[['joy_values', 'positive_values', 'trust_values', 'anticipation_values']].idxmax(axis=1)
    
    return df
        

def heatmap(df_word_analyzed):
    columns_of_interest = ['joy_values', 'anticipation_values', 'trust_values', 'positive_values']
    df_subset = df_word_analyzed[columns_of_interest]
    correlation_matrix = df_subset.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
   
def extract_keywords(df_word_analyzed):
    # Convert the string representation of lists to actual lists
    df_word_analyzed['happy_words'] = df_word_analyzed['happy_words'].apply(literal_eval)
    all_happy_words = [word for sublist in df_word_analyzed['happy_words'].tolist() for word in sublist]
    top_10_happy_words = pd.Series(all_happy_words).value_counts().head(10).index.tolist()
    return top_10_happy_words


        

# In[ ]:




