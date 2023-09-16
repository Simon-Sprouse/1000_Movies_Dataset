#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 19:24:17 2023

@author: simonsprouse
"""

import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
import string
import re

def compTitles(title1, title2):
    return SequenceMatcher(None, title1, title2).ratio()

def jaccardIndex(real_title, comp_title):
    
    real_title_ls = [str.lower(word).strip(string.punctuation) for word in real_title.split(sep=" ")]
    comp_title_ls = [str.lower(word).strip(string.punctuation) for word in comp_title.split(sep=" ")]
    
    set1 = set(real_title_ls)
    set2 = set(comp_title_ls)

    j_index = len(set1.intersection(set2)) / len(set1.union(set2))
    
    return j_index

def findUrl(title, date):

    # search = "The Wolf of Wallstreet"
    # date = "2013"
    search = title.replace(" ", "+")
    search += "+%28{}%29".format(date)
    
    
    url = "https://www.springfieldspringfield.co.uk/movie_scripts.php?search=" + search
    
    response = requests.get(url)
    
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    best = (0, "None (0000)")
    tags = soup.findAll('a', class_="btn btn-dark btn-sm")
    for tag in tags:
        tag_date = tag.text[len(tag.text) - 5:len(tag.text) - 1]
        tag_no_date = tag.text[:len(tag.text) - 7]

        similarity = jaccardIndex(title, tag_no_date)
        if tag_date == date:
            similarity += 1
        print(similarity)
        if similarity > best[0]:
            best = (similarity, tag.text)
            
    print(best)
    
    title = best[1]
    query = str.lower(title.replace(" ", '-'))[:len(title) - 7]
    query = re.sub(r'[^a-zA-Z0-9\s-]', "", query)
    
    return query
    
    


query = findUrl("The Dark Knight", "2008")
print(query)
        


