#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 19:24:17 2023

@author: simonsprouse
"""

import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

def compTitles(title1, title2):
    return SequenceMatcher(None, title1, title2).ratio()

def findUrl(search, date):

    # search = "The Wolf of Wallstreet"
    # date = "2013"
    search = search.replace(" ", "+")
    search += "+%28{}%29".format(date)
    
    
    url = "https://www.springfieldspringfield.co.uk/movie_scripts.php?search=" + search
    
    response = requests.get(url)
    
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    best = (0, "None (0000)")
    tags = soup.findAll('a', class_="btn btn-dark btn-sm")
    for tag in tags:
        similarity = compTitles(search, tag.text)
        print(similarity)
        if similarity > best[0]:
            best = (similarity, tag.text)
            
    print(best)
    
    title = best[1]
    query = str.lower(title.replace(" ", '-'))[:len(title) - 7]
    
    return query
    
    


query = findUrl("The Dark Knight", "2008")
print(query)
        


