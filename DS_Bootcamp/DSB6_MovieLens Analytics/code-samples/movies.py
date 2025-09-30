import sys
import os
import urllib
import urllib.request
import requests
import collections
import functools
import datetime
import re
import bs4
import json


class Movies:
    """
    Analyzing data from movies.csv
    """
    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        with open(path_to_the_file, 'r') as file:
            self.data = file.readlines()
        
    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts. 
        You need to extract years from the titles. Sort it by counts descendingly.
        """
        release_years = collections.Counter()
        for movie in self.data:
            year = self.extract_year(movie['title'])
            release_years[year] += 1
        release_years = collections.OrderedDict(sorted(release_years.items(), key=lambda x: x[1], reverse=True))
        return release_years # maybe change naming
    
    def extract_year(self, title):
        match_item = re.search(r'\((\d{4})\)', title)
        if match_item:
            return int(match_item.group(1)) 
    
    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
     Sort it by counts descendingly.
        """
        return genres
        
    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and 
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        return movies

if __name__ == "__main__":
    movie = Movies("../src/ml-latest-small/movies.csv")