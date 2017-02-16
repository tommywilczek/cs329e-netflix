import pickle
import Netflix
from os import listdir
from os.path import isfile, join
    
unique_customer_ids_cache_filename = "grm695_wjc656_unique_cust_ids.p"

def update_dict(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    else:
        dictionary[key] += value

def read_all_movies():
    total_customer_skew = dict()
    num_movies_seen = dict()
    average_movie_ratings = Netflix.netflix_read_file("netflix-tests/ccm2555_ar53446_movie_avg_rating.pickle")
    average_customer_skew = dict()

    training_set_path = '/u/downing/public_html/netflix/training_set/'
    unique_customer_ids_cache = Netflix.netflix_read_file("netflix-tests/" + unique_customer_ids_cache_filename)
    i = 0
    for filename in listdir(training_set_path):
        
        full_path = join(training_set_path, filename)
        if isfile(full_path):
            movie_id, movie_ratings = read_mv_file(full_path)
            for cust_id, rating in movie_ratings.items():
                if cust_id in unique_customer_ids_cache:
                    skew = float(rating) - average_movie_ratings[movie_id]
                    update_dict(total_customer_skew, cust_id, skew)
                    update_dict(num_movies_seen, cust_id, 1)
        i += 1
        if i % 100 == 0:
            print(i)

    for cust_id in total_customer_skew:
        average_customer_skew[cust_id] = round(total_customer_skew[cust_id] / num_movies_seen[cust_id], 2)

    return average_customer_skew

    print("Average customer skew: ", average_customer_skew)

def read_mv_file(filename):
    movie_ratings = dict()
    movie_id = -1

    with open(filename) as mv_file:
        lines = mv_file.readlines()
        
        for line in lines:
            line = line.strip()
            if ":" in line:
                movie_id = int(line[:len(line) - 1])
            else:
                cust_id = -1
                rating = -1

                values = line.split(",")
                assert len(values) == 3
                cust_id = int(values[0])
                rating = int(values[1])
                movie_ratings[cust_id] = rating

    return (movie_id, movie_ratings)

def read_all_customer_ids(input_filename):
    with open(input_filename) as input_file:
        unique_customer_ids = set()
        lines = input_file.readlines()  
        for line in lines:
            if ":" not in line:
                customer_id = int(line.strip())
                unique_customer_ids.add(customer_id)
        return unique_customer_ids

def make_average_customer_skew_cache():
    # Create a cache of average customer skews
    cache_filename = "grm695_wjc656_avg_cust_skew.p"
    cache_path = join("netflix-tests/", cache_filename)
    cache = read_all_movies()
    with open(cache_path, "wb") as cache_file:
        pickle.dump(cache, cache_file, protocol=pickle.HIGHEST_PROTOCOL)

def make_unique_customer_id_cache():
    # Create a cache of average customer skews
    global unique_customer_ids_cache_filename
    cache_path = join("netflix-tests/", unique_customer_ids_cache_filename)
    input_filename = "data/probe.txt"
    cache = read_all_customer_ids(input_filename)
    with open(cache_path, "wb") as cache_file:
        pickle.dump(cache, cache_file, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__" :
    #make_test_case("data/mv_0002043.txt")
    make_average_customer_skew_cache()
    #make_unique_customer_id_cache()