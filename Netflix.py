#!/usr/bin/env python3

# -------
# imports
# -------

from math import sqrt
import pickle
from requests import get
from os import path
from numpy import sqrt, square, mean, subtract


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

"""
AVERAGE_RATING = 3.60428996442
ACTUAL_CUSTOMER_RATING = create_cache(
    "cache-actualCustomerRating.pickle")
AVERAGE_MOVIE_RATING_PER_YEAR = create_cache(
    "cache-movieAverageByYear.pickle")
YEAR_OF_RATING = create_cache("cache-yearCustomerRatedMovie.pickle")
CUSTOMER_AVERAGE_RATING_YEARLY = create_cache(
    "cache-customerAverageRatingByYear.pickle")

decade_avg_cache = create_cache("cache-actualCustomerRating.pickle")
movie_year_cache = create_cache("kzk66-movies_and_years.pickle")
actual_scores_cache = create_cache("kzk66-year_rating_avg.pickle")

"""
actual_scores_cache =create_cache(
    "cache-actualCustomerRating.pickle")
movie_year_cache = create_cache("cache-yearCustomerRatedMovie.pickle")
average_movie_rating_per_year = create_cache(
    "cache-movieAverageByYear.pickle")
customer_average_rating_yearly = create_cache(
    "cache-customerAverageRatingByYear.pickle")
decade_avg_cache = {1990: 2.4}

# ------------
# netflix_eval
# ------------

def netflix_eval(reader, writer) :
    
    """print ("ACTUAL SCORES CACHE!!!!!!!!!!!!!!!!!!!!!!")
    #print (actual_scores_cache)# (723633, 10561): 3....user,movie,rating
    print ("movie_year_cache!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print (movie_year_cache)# (1065162, 15449): 2005.....user,movie,when
    print ("average_movie_rating_per_year!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print (average_movie_rating_per_year)#looks like (2034850, 2002): 3.743
    print ("customer_average_rating_yearly!!!!!!!!!!!!!!!!!!!!!!!")
    #print (customer_average_rating_yearly)#looks like (2236702, 2001): 4.174
    print ("decade_avg_cache!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print (decade_avg_cache)
"""
   
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

            '''
            pred = int(movie_year_cache[int(current_movie)])
            pred = (pred // 10) *10
            prediction = decade_avg_cache[pred]
            writer.write(line)
            writer.write('\n')
            '''
        else:
		# It's a customer
            current_customer = line
            print("CURRENT CUSTOMER", type(current_customer))
            counter = 0
            sum_total = 0
            for key in customer_average_rating_yearly:
                #print ((key[0]))
                if (int(current_customer) == key[0]):
                    print("IT WORKS!", key, (customer_average_rating_yearly[key]))
                    counter += 1
                    sum_total+= customer_average_rating_yearly[key]
            sum_total /= counter
            return (sum_total)
                    


            """
            predictions.append(prediction)
            actual.append(actual_scores_cache[int(current_movie)][int(current_customer)])
            writer.write(str(prediction)) 
            writer.write('\n')
            """	
    """# calculate rmse for predications and actuals
    rmse = sqrt(mean(square(subtract(predictions, actual))))
    writer.write(str(rmse)[:4] + '\n')
"""

