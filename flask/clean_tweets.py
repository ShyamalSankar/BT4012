import pandas as pd
import tweepy
import re
import numpy as np
import os
import demoji
import emoji
import string
from bs4 import BeautifulSoup
from langdetect import detect
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
stopwords = nltk.corpus.stopwords.words('english')

def preprocess(text):
    #remove emojis and store decoded emojis in list
    all_emojis = emoji_code_text(text)
    text = ''.join(x for x in text if not emoji.is_emoji(x))
    #remove url
    pattern = r'(https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}[-a-zA-Z0-9()@:%_+.~#?&/=]*)' 
    text = re.sub(pattern, '', text)
    text = text.strip()
    text = text.lower()
    #text = word_tokenize(text)
    text = text.split(' ')
    text = [w for w in text if not w in stopwords]
    final_text = []
    for word in text:
        #check useraccount
        if word.startswith("@"):
            final_text.append("__user_mention__")
        #check hashtag
        elif word.startswith("#"):
            final_text.append("__hashtag__")
        else:
            final_text.append(lemmatizer.lemmatize(word))
    final_text = final_text + all_emojis
    return " ".join(word for word in final_text)

def emoji_code_text(text):
    all_emojis = ''.join(x for x in text if emoji.is_emoji(x))
    #emoji_dict = dict()
    emoji_word_list = []
    try:
        #For each emoji, decode it and add the decoding into the list
        for each_emoji in all_emojis:
            decoded = emoji.demojize(each_emoji)
            decoded = decoded.replace(':', '')
            emoji_word_list.append(decoded)
    except UnicodeDecodeError:
        emoji_word_list = []
        #df["emoji"][word] = dict()
        #df["emoji_text"][word] = []
    return emoji_word_list

def remove_punctuation(text):
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree

def remove_nonalphanum(text):
    return re.sub("[^a-z0-9]","", text)
