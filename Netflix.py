#!/usr/bin/env python3

# -------
# imports
# -------

from math import sqrt
import pickle
import time
from requests import get
from os import path
from numpy import sqrt, square, mean, subtract

start = time.time()
def create_cache(filename):
    """
    filename is the name of the cache file to load
    returns a dictionary after loading the file or pulling the file from the public_html page
    """
    cache = {}
    filePath = "/u/fares/public_html/netflix-caches/" + filename

    if path.isfile(filePath):
        with open(filePath, "rb") as f:
            cache = pickle.load(f)
    else:
        webAddress = "http://www.cs.utexas.edu/users/fares/netflix-caches/" + \
            filename
        bytes = get(webAddress).content
        cache = pickle.loads(bytes)

    return cache

#caches used to evaluate data and find RMSE
actual_scores_cache =create_cache(
    "cache-actualCustomerRating.pickle")
customer_avg_rating = create_cache(
    "mmm5589_customer_avg_rating.pickle")
movie_average_rating = create_cache(
    "rs45899-movieAverageRating.pickle")
movie_sd = create_cache(
    "krk893-njf388-CustomerSTDDiff.pickle")#1048577: 0.93180212486409597

# ------------
# netflix_eval
# ------------

def netflix_eval(reader, writer) :
    #print (movie_sd)
    #return
    predictions = []
    actual = []
    # iterate throught the file reader line by line
    for line in reader:
    # need to get rid of the '\n' by the end of the line
        line = line.strip()
        # check if the line ends with a ":", i.e., it's a movie title 
        if line[-1] == ':':
		# It's a movie
            current_movie = line.rstrip(':')
            #pulls from average movie rating cache
            ratings = movie_average_rating[int(current_movie)]
            writer.write(line)
            writer.write('\n')
            
        else:
		# It's a customer
            current_customer = line
            standDev = movie_sd[int(current_customer)]
            fixed_customer_rating = round((ratings + standDev), 2)

            
            #figure out actual scores
            ##value = actual_scores_cache[int(current_movie), int(current_customer)]
            predictions.append((fixed_customer_rating))
            #Problem below: TypeError: 'dict' object is not callable
            actual_temp = actual_scores_cache[int(current_customer),int(current_movie)]
            #print ("actual_temp", actual_temp)
            actual.append(actual_temp)
            writer.write(str(fixed_customer_rating)) 
            writer.write('\n')
    # calculate rmse for predications and actuals
    rmse = sqrt(mean(square(subtract(predictions, actual))))
    end = time.time()
    writer.write(str(rmse)[:4] + '\n')

