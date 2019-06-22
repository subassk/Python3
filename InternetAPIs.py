This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).
You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)
To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather than requests.get(). If you’re having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists in our cache. We will try to provide as much information as we can to help guide you to form queries for which data exists in the cache.
Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.
Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.
Try invoking your function with the input “Black Panther”.
HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. If any other parameters are included, then the function will not be able to recognize the data that you’re attempting to pull from the cache. Remember, you will not need an api key in order to complete the project, because all data will be found in the cache.
The cache includes data for the following queries:

q	type	limit
Black Panther	<omitted>	<omitted>
Black Panther	<omitted>	5
Black Panther	movies	<omitted>
Black Panther	movies	5
Tony Bennett	<omitted>	5
Tony Bennett	movies	5
Captain Marvel	movies	5
Bridesmaids	movies	5
Sherlock Holmes	movies	5


import requests_with_caching
import json
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")

def get_movies_from_tastedive(movie_name):
    parameters = {"q": movie_name, "type": "movies", "limit": "5"}
    tastedive = requests_with_caching.get("https://tastedive.com/api/similar", params = parameters)
    # tastedive = requests_with_caching.get()    
    # print(tastedive["Similar"])
    return tastedive.json()

get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")

Output:
found in permanent_cache
found in permanent_cache
found in permanent_cache
found in permanent_cache
found in permanent_cache
found in permanent_cache

Data file: this_page_cache.txt
{
  "https://tastedive.com/api/similarlimit-5_q-Bridesmaids_type-movie": "Failed to retrieve that URL",
  "https://tastedive.com/api/similarlimit-5_q-Black Panther_type-movie": "Failed to retrieve that URL",
  "https://tastedive.com/api/similarlimit-5_q-Tony Bennett_type-movie": "Failed to retrieve that URL",
  "https://tastedive.com/api/similarlimit-5_q-undefined_type-movies": "Failed to retrieve that URL"
}

Result	Actual Value	Expected Value	Notes
Pass	5	5	Testing that get_movies_from_tastedive returns only 5 results
Pass	0	0	Testing that get_movies_from_tastedive retrieves only movies and not music.
Pass	'Bridesmaids'	'Bridesmaids'	Testing that the results for Bridesmaids is the expected result.
Pass			Testing that the correct python type is returned.
You passed: 100.0% of the tests


    
//Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.

import requests_with_caching
import json
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))
def get_movies_from_tastedive(movie_name):
    parameters = {"q": movie_name, "type": "movies", "limit": "5"}
    tastedive = requests_with_caching.get("https://tastedive.com/api/similar", params = parameters)
    return tastedive.json()

#get_movies_from_tastedive("Bridesmaids")
#get_movies_from_tastedive("Black Panther")

print(get_movies_from_tastedive("Tony Bennett")) 

def extract_movie_titles(queryResult):
    list = []
    for d in queryResult['Similar']['Results']:
        list.append(d['Name'])
    return list
print(list)

extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))

Output:
found in permanent_cache
{'Similar': {'Info': [{'Name': 'Tony Bennett', 'Type': 'music'}], 'Results': [{'Name': 'The Startup Kids', 'Type': 'movie'}, {'Name': 'Charlie Chaplin', 'Type': 'movie'}, {'Name': 'Venus In Fur', 'Type': 'movie'}, {'Name': 'Loving', 'Type': 'movie'}, {'Name': 'The African Queen', 'Type': 'movie'}]}}
<class 'list'>
found in permanent_cache
found in permanent_cache
found in permanent_cache

Result	Actual Value	Expected Value	Notes
Pass	"['The...een']"	"['The...een']"	Testing that correct results are returned for extract_movie_titles(get_movies_from_tastedive("Tony Bennett").
You passed: 100.0% of the tests


