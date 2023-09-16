#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:07:19 2023

@author: simonsprouse
"""

import requests
from bs4 import BeautifulSoup
import string


def getScript(title):

    title = str.lower(title.replace(" ", '-'))
    
    ## url = "https://www.springfieldspringfield.co.uk/movie_script.php?movie={}".format(title)

    url = 'https://www.springfieldspringfield.co.uk/movie_script.php?movie=the-wolf-of-wall-street'
    response = requests.get(url)

    
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.findAll('div', class_='scrolling-script-container')
    

    for div in container:
        ## print(div.text)
        return div.text

        
    return ""
        
        
script = getScript("Godfather-the")
print(script)

file = open("swear.txt")
    
swears = [line.rstrip('\n') for line in file.readlines()]
print(swears)

count = 0

for word in script.split(sep=' '):
    print(str.lower(word).rstrip(string.punctuation))
    if str.lower(word).rstrip(string.punctuation) in swears:
        count += 1

print(count)