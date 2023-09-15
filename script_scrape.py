#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:07:19 2023

@author: simonsprouse
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.springfieldspringfield.co.uk/movie_script.php?movie=up"

response = requests.get(url)
# print(response.text)


soup = BeautifulSoup(response.text, 'html.parser')

container = soup.findAll('div', class_='scrolling-script-container')

# for div in container:
#     print(div.text)
    
print(container[0].text)