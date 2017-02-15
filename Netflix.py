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

movie_average_rating = create_cache(
    "rs45899-movieAverageRating.pickle")

# ------------
# netflix_eval
# ------------

def netflix_eval(reader, writer) :

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
            print('Current Movie', current_movie)
            print('Its rating', movie_average_rating[int(current_movie)])
            ratings = movie_average_rating[int(current_movie)]

                    
            print ("RATINGS:   ", ratings)
            ##pred = int(movie_year_cache[int(current_movie)])
            ##pred = (pred // 10) *10
            ##prediction = decade_avg_cache[pred]

            writer.write(line)
            writer.write('\n')
            
        else:
		# It's a customer


        
            current_customer = line
            print("CURRENT CUSTOMER", (current_customer))

            '''
            #Took from movie if statement
            for key in movie_average_rating:
                #print ("KEY", key)
                if int(current_movie) == int(key):
                    ratings.append(movie_average_rating[int(current_movie)])
                    break   

            print("CURRENT CUSTOMER", type(current_customer))
            counter = 0 #counts number of times the movie was reviewed in years
            sum_total = 0
            for key in movie_average_rating: #go through each year movie rating in the cache
                print("IT WORKS!", key, (movie_average_rating[key]))
                counter += 1
                sum_total+= movie_average_rating[key]
            #if (counter == 0):
            #    continue            
            sum_total /= counter #Get the average rating across all years
            print(sum_total)
            predictions.append(sum_total)
 
            '''
            #figure out actual scores
            ##value = actual_scores_cache[int(current_movie), int(current_customer)]
            predictions.append(ratings)
            #Problem below: TypeError: 'dict' object is not callable
            actual_temp = actual_scores_cache[int(current_customer),int(current_movie)]
            print ("actual_temp", actual_temp)
            actual.append(actual_temp)
            '''
            value = ratings
            if (ratings != []):
                value = actual_scores_cache[int(current_customer), int(current_movie)]
            print('Value', value)
            actual.append(value)
            '''

            writer.write(str(ratings)) 
            writer.write('\n')


    # calculate rmse for predications and actuals
    print ("PREDICTIONS: ",predictions)
    print ()
    print ("ACTUAL IS",actual) 
    rmse = sqrt(mean(square(subtract(predictions, actual))))
    print ("AND THE RMSE ISSSSS.....",rmse)
    writer.write(str(rmse)[:4] + '\n')


"""
(1581659, 2612): 2, (772771, 12047): 2, (488926, 14430): 4, (373299, 11328): 4,
 (2526957, 16967): 4, (659118, 4207): 5, (453940, 710): 5, (723633, 10561): 3, (1306039, 16969): 5, (1961294, 1046): 4, (2269919, 10027): 3,
 (1535639, 15871): 4, (97749, 16262): 5, (424128, 3917): 5, (1065162, 15449): 4,
  (1548873, 12501): 5, (792128, 1865): 4, (2185412, 11903): 5
  """