#!/usr/bin/env python
# coding: utf-8

# In[2]:



import pip    
import pandas as pd
import matplotlib.pyplot as plt
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

# Upgrade Pillow
run_command("python3 -m pip install --upgrade Pillow")

def install(package):
    pip.main(['install', package])

# Ensure wordcloud is installed
try:
    import wordcloud
except ImportError:
    install('wordcloud')
    import wordcloud

from wordcloud import WordCloud, STOPWORDS

def word_cloud(df):
    stopwords = set(STOPWORDS)
    s = {"happy", "got", "went", "made", "able", "one", "good" }
    for word in s: 
        if word not in stopwords: 
            stopwords.add(word)
    text = ' '.join(df['cleaned_hm'].tolist())
    text = text.lower()
    wordcloud = WordCloud(background_color="white", height=2700, width=3600, contour_width = 0.5, stopwords = stopwords).generate(text)
    plt.figure( figsize=(14,8) )
    plt.imshow(wordcloud.recolor(colormap=plt.get_cmap('Set2')), interpolation='bilinear')
    plt.axis("off")

# In[ ]:




