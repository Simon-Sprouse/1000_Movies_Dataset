#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:59:36 2023

@author: simonsprouse
"""

import requests
import json


def getID(title):
    """ Sends GET request to TMDB and returns Id's for movie title """
    
    title.replace(" ", "%")
    
    url = "https://api.themoviedb.org/3/search/movie?query={}&include_adult=false&language=en-US&page=1".format(title)
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Y2JlYzFjZmFiNGExYjU2YzY0NjMyNGI1MTg5MTVlZiIsInN1YiI6IjY0ZjI1ZGNkZTBjYTdmMDBhZTM5YzdhZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Mat5xSeWLIco-N24HGrTbBvtQMWM85sR1DHOrDezYQ0"
    }
    
    ## GET Request to TMDB server
    response = requests.get(url, headers=headers)
    response_text = response.text
    parse = json.loads(response_text)
    results = parse['results'] ## parsed results return as Json/Dict
    
    
    ## Select the movie that matches title the best
    if len(results) > 0: 
        best_match = results[0]
        movie_id = best_match['id']
        genre_ids = best_match['genre_ids']
        
        return (movie_id, genre_ids)
    
    else: 
        return (None, None)

print(getID("The Lion King"))



