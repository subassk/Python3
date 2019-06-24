#//This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).
#You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)
#To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather than requests.get(). If you’re having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists in our cache. We will try to provide as much information as we can to help guide you to form queries for which data exists in the cache.
#Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.
#Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.
#Try invoking your function with the input “Black Panther”.
#HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. If any other parameters are included, then the function will not be able to recognize the data that you’re attempting to pull from the cache. Remember, you will not need an api key in order to complete the project, because all data will be found in the cache.
#The cache includes data for the following queries:

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


    
#//Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.

import requests_with_caching
import json
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))
def get_movies_from_tastedive(movie_name):
    parameters = {"q": movie_name, "type": "movies", "limit": "5"}
    tastedive = requests_with_caching.get("https://tastedive.com/api/similar", params = parameters)
    return tastedive.json()
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


#//Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.
import requests_with_caching
import json
def get_movies_from_tastedive(movie_name):
    parameters = {"q": movie_name, "type": "movies", "limit": "5"}
    tastedive = requests_with_caching.get("https://tastedive.com/api/similar", params = parameters)
    return tastedive.json()

print(get_movies_from_tastedive("Tony Bennett")) 
def extract_movie_titles(queryResult):
    list = []
    for d in queryResult['Similar']['Results']:
        list.append(d['Name'])
    return list

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])

def get_related_titles(list):
    final_list = []
    for title in list:
        for item in extract_movie_titles(get_movies_from_tastedive(title)):
            final_list.append(item)
    print(final_list)               
    return_list = []

    for item in final_list:
        if item not in return_list:
            return_list.append(item)
    return return_list
get_related_titles(["Black Panther", "Captain Marvel"])
get_related_titles([])
                                                                                                           
Output:                                                                                                           
found in permanent_cache
{'Similar': {'Info': [{'Name': 'Tony Bennett', 'Type': 'music'}], 'Results': [{'Name': 'The Startup Kids', 'Type': 'movie'}, {'Name': 'Charlie Chaplin', 'Type': 'movie'}, {'Name': 'Venus In Fur', 'Type': 'movie'}, {'Name': 'Loving', 'Type': 'movie'}, {'Name': 'The African Queen', 'Type': 'movie'}]}}
found in permanent_cache
found in permanent_cache
found in permanent_cache
found in permanent_cache
['Captain Marvel', 'Avengers: Infinity War', 'Ant-Man And The Wasp', 'The Fate Of The Furious', 'Deadpool 2', 'Inhumans', 'The Fate Of The Furious', 'Venom', 'American Assassin', 'Black Panther']
[]
found in permanent_cache
found in permanent_cache
['Captain Marvel', 'Avengers: Infinity War', 'Ant-Man And The Wasp', 'The Fate Of The Furious', 'Deadpool 2', 'Inhumans', 'The Fate Of The Furious', 'Venom', 'American Assassin', 'Black Panther']
[]

Result	Actual Value	Expected Value	Notes
Pass	[]	[]	Testing that the correct response is returned when no titles are included.
Pass	"['Cap...her']"	"['Cap...her']"	Testing that the correct response is returned when searching for Black Panther and Captain Marvel.
You passed: 100.0% of the tests

                                                                                                           
//Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.
Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache.

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")
import requests_with_caching
import json
import requests

def get_movie_data(input):
    base_url = 'http://www.omdbapi.com/'
    parms_dict = {}
    parms_dict['apikey'] = 'mykey'
    parms_dict['t'] = input
    parms_dict['r'] = 'json'
    #movie_data = requests_with_caching.get(base_url, params = {'t':input, 'r':'json'})
    #movie_data = requests_with_caching.get('http://www.omdbapi.com/', params = {'t':input, 'r':'json'})
    movie_data = requests_with_caching.get(base_url, params = parms_dict)
    return movie_data.json()
get_movie_data("Venom")
get_movie_data("Baby Mama")

Output:                                                                                                           
found in permanent_cache
found in permanent_cache
found in permanent_cache
found in permanent_cache
                                                                                                           
Result	Actual Value	Expected Value	Notes
Pass			Testing that the correct python type is returned.
Pass	'Baby Mama'	'Baby Mama'	Testing that the results match the query.
You passed: 100.0% of the tests
                                                                                                           
                                                                                                           
 //Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.                                                                                                          
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))
import requests_with_caching
import json

def get_movie_data(input):
    movie_data = requests_with_caching.get('http://www.omdbapi.com/', params = {'t':input, 'r':'json'})
    return movie_data.json()

#Way 1:(ERROR)
#def get_movie_rating(input):
#    try:
#        if input['Ratings']:
#            if input['Ratings'][1]['Value'].replace('%','').isnumeric():
#                movie_rating = int(input['Ratings'][1]['Value'].replace('%',''))
#                return movie_rating
#        return 0
#    except IndexError as idx:
#        return 0


#Way 2:(ERROR)
#def get_movie_rating(a):
#    movieData = get_movie_data(input)
#    RTrating = 0
#    for each in movieData['Ratings']:
#        if each['Source'] != 'Rotten Tomatoes':
#            continue
#        else:
#            RTrating = each['Value'].replace('%','')    
#    return int(RTrating)


#Way 3:
def get_movie_rating(dictionary):
    if dictionary["Ratings"][1]["Source"] ==  "Rotten Tomatoes":
        print(dictionary["Ratings"][1]["Value"][0:2])
        return int(dictionary["Ratings"][1]["Value"][0:2])
    else:
        return 0

get_movie_rating(get_movie_data("Deadpool 2"))

Output:                                                                                                          
found in permanent_cache
83
found in permanent_cache
found in permanent_cache
83
found in permanent_cache
83
                                                                                                           
Result	Actual Value	Expected Value	Notes
Pass	0	0	Testing that the code is acurate for Venom (no rating).
Pass	83	83	Testing that the code for 'Deadpool 2'.
Pass			Testing that a dictionary is returned.
You passed: 100.0% of the tests
                                                                                                           
//Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
                                                                                                           
                                                                                                           
