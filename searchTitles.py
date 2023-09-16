#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 19:24:17 2023

@author: simonsprouse
"""

import requests
from bs4 import BeautifulSoup
import string
import re


def jaccardIndex(real_title, comp_title):
    '''
    Computes the similarity between two strings
    
    '''
    
    ## prepare strings to be compared
    real_title_ls = [str.lower(word).strip(string.punctuation) for word in real_title.split(sep=" ")]
    comp_title_ls = [str.lower(word).strip(string.punctuation) for word in comp_title.split(sep=" ")]
    
    ## create set of each word
    set1 = set(real_title_ls)
    set2 = set(comp_title_ls)

    ## compute intersection / union
    j_index = len(set1.intersection(set2)) / len(set1.union(set2))
    
    return j_index

def findUrl(title, date):
    '''
    Takes a movie title and returns the url for the best match
    
    '''
    
    ## Generate possible titles using request to database
    search = title.replace(" ", "+")
    search += "+%28{}%29".format(date)
    url = "https://www.springfieldspringfield.co.uk/movie_scripts.php?search=" + search
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    ## will track the most similar entry
    best = (0, "None (0000)")
    
    ## target query results
    tags = soup.findAll('a', class_="btn btn-dark btn-sm")
    for tag in tags:
        
        ## remove date from query result and find j-index
        tag_no_date = tag.text[:len(tag.text) - 7]
        similarity = jaccardIndex(title, tag_no_date)
        
        ## add +1 to all movies released in the correct year
        tag_date = tag.text[len(tag.text) - 5:len(tag.text) - 1]
        if tag_date == date:
            similarity += 1
        
        ## update best
        if similarity > best[0]:
            best = (similarity, tag.text)
            
    ## format the best result
    title = best[1]
    query = str.lower(title.replace(" ", '-'))[:len(title) - 7]
    query = re.sub(r'[^a-zA-Z0-9\s-]', "", query)
    
    return query
    
    


query = findUrl("The Dark Knight", "2008")
print(query)
        


