#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:59:36 2023

@author: simonsprouse
"""

import requests
import json


title = "Lion King"
title.replace(" ", "%")

url = "https://api.themoviedb.org/3/search/movie?query={}&include_adult=false&language=en-US&page=1".format(title)

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Y2JlYzFjZmFiNGExYjU2YzY0NjMyNGI1MTg5MTVlZiIsInN1YiI6IjY0ZjI1ZGNkZTBjYTdmMDBhZTM5YzdhZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Mat5xSeWLIco-N24HGrTbBvtQMWM85sR1DHOrDezYQ0"
}

response = requests.get(url, headers=headers)


response_text = response.text
# print(response_text)


y = json.loads(response_text)

results = y['results']

if len(results) > 0: 
    best_match = y['results'][0]
    print(best_match)

