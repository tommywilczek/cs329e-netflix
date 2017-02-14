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

#print (average_movie_rating_per_year)
#average_movie_rating_per_year: (4690, 2002): 3.181
#                               (movie, year): rating 



def chill():
    final_cache = {}
    cache_counter = 0
    for key in average_movie_rating_per_year:
        movie_average = 0
        averager = 0
        cache_counter += 1
        counter = 0
        movie = key[0]
        


        #for key1 in range (cache_counter, len(average_movie_rating_per_year)):
        for key1 in average_movie_rating_per_year: 
            for key3 in final_cache:
                if key3 == key1:
                    continue
                 
                if key1[0] == movie:
                    counter += 1
                    print("movie", movie)
                    rating = average_movie_rating_per_year[key]
                    averager +=rating 
            #movie_average /= counter
            final_cache = {movie: movie_average}

    final_cache = {(movie): ''}

chill()