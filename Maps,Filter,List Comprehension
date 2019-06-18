//Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” to the beginning of each element using mapping.

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing = map(lambda item:'Fruit: '+ item,lst_check)
print(map_testing)

Output:
['Fruit: plums', 'Fruit: watermelon', 'Fruit: kiwi', 'Fruit: strawberries', 'Fruit: blueberries', 'Fruit: peaches', 'Fruit: apples', 'Fruit: mangos', 'Fruit: papaya']

Result	Actual Value	Expected Value	Notes
Pass	"['Fru...aya']"	"['Fru...aya']"	Testing that map_testing has the correct values.
Pass	'map('	'\nlst_...ting)'	Testing your code (Don't worry about actual and expected values).
Pass	'filter('	'\nlst_...ting)'	Testing your code (Don't worry about actual and expected values).
Pass	'sum('	'\nlst_...ting)'	Testing your code (Don't worry about actual and expected values).
Pass	'zip('	'\nlst_...ting)'	Testing your code (Don't worry about actual and expected values).
You passed: 100.0% of the tests



//Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only contains the strings from countries that begin with B.
item
countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = []
b_countries = filter(lambda item:'B' in item,countries)
print(b_countries)

Output:
['Brazil', 'Botswana', 'Britain', 'Bangladesh', 'Belarus', 'Belgium']

Result	Actual Value	Expected Value	Notes
Pass	"['Bra...ium']"	"['Bra...ium']"	Testing that b_countries is correct.
Pass	'map('	'\ncoun...ries)'	Testing your code (Don't worry about actual and expected values).
Pass	'filter('	'\ncoun...ries)'	Testing your code (Don't worry about actual and expected values).
Pass	'sum('	'\ncoun...ries)'	Testing your code (Don't worry about actual and expected values).
Pass	'zip('	'\ncoun...ries)'	Testing your code (Don't worry about actual and expected values).
You passed: 100.0% of the tests


//Below, we have provided a list of tuples that contain the names of Game of Thrones characters. Using list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names = []
first_names = [name[1] for name in people]
print(first_names)

Output:
['Jon', 'Cersei', 'Arya', 'Robb', 'Jamie', 'Daenerys', 'Sansa', 'Margaery', 'Eddard', 'Tyrion', 'Joffrey', 'Ramsey', 'Peter']

Result	Actual Value	Expected Value	Notes
Pass	"['Jon...ter']"	"['Jon...ter']"	Testing that first_names is correct.
Pass	'map('	'\npeop...ames)'	Testing your code (Don't worry about actual and expected values).
Pass	'filter('	'\npeop...ames)'	Testing your code (Don't worry about actual and expected values).
Pass	'sum('	'\npeop...ames)'	Testing your code (Don't worry about actual and expected values).
Pass	'zip('	'\npeop...ames)'	Testing your code (Don't worry about actual and expected values).
You passed: 100.0% of the tests


//Use list comprehension to create a list called lst2 that doubles each element in the list, lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [(item + item) for item in lst]
print(lst2)

Output:
[['hi', 'bye', 'hi', 'bye'], 'hellohello', 'goodbyegoodbye', [9, 2, 9, 2], 8]

Result	Actual Value	Expected Value	Notes
Pass	"[['hi...], 8]"	"[['hi...], 8]"	Testing that lst2 is assigned to correct values
Pass	'map('	'\nlst ...st2)\n'	Testing your code (Don't worry about actual and expected values).
Pass	'filter('	'\nlst ...st2)\n'	Testing your code (Don't worry about actual and expected values).
Pass	'sum('	'\nlst ...st2)\n'	Testing your code (Don't worry about actual and expected values).
Pass	'zip('	'\nlst ...st2)\n'	Testing your code (Don't worry about actual and expected values).
You passed: 100.0% of the tests


//Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. Using list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [tuple_Pair[0] for tuple_Pair in students if tuple_Pair[1] >= 70]
print(passed)

output:
['Tommy', 'Carl', 'Bob', 'Sue']

Result	Actual Value	Expected Value	Notes
Pass	"['Tom...Sue']"	"['Tom...Sue']"	Testing that passed is correct.
Pass	'map('	'\nstud...sed)\n'	Testing your code (Don't worry about actual and expected values).
Pass	'filter('	'\nstud...sed)\n'	Testing your code (Don't worry about actual and expected values).
Pass	'sum('	'\nstud...sed)\n'	Testing your code (Don't worry about actual and expected values).
Pass	'zip('	'\nstud...sed)\n'	Testing your code (Don't worry about actual and expected values).
You passed: 100.0% of the tests


//Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
print(list(zip(l1,l2)))
opposites = list(filter(lambda tuple : len(tuple[0]) > 3 and len(tuple[1]) > 3, zip(l1,l2)))
print(opposites)

Output:
[('left', 'right'), ('up', 'down'), ('front', 'back')]
[('left', 'right'), ('front', 'back')]

Result	Actual Value	Expected Value	Notes
Pass	"[('le...ck')]"	"[('le...ck')]"	Testing that opposites has the correct list of tuples.
Pass	'map('	'\nl1 =...ites)'	Testing your code (Don't worry about actual and expected values).
Pass	'filter('	'\nl1 =...ites)'	Testing your code (Don't worry about actual and expected values).
Pass	'sum('	'\nl1 =...ites)'	Testing your code (Don't worry about actual and expected values).
Pass	'zip('	'\nl1 =...ites)'	Testing your code (Don't worry about actual and expected values).
You passed: 100.0% of the tests


//Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this list, create a new list called endangered that contains the names of species whose populations are below 2500.
species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info=zip(species,population)

#Using Map,Filter
endangered = list(map (lambda tuple: tuple[0], filter (lambda tuple : tuple[1] < 2500, pop_info)))
#endangered = list(map (lambda tuple: tuple[0], filter (lambda tuple : tuple[1] < 2500, pop_info)))

#Using List comprehension
endangered = [tuple[0] for tuple in pop_info if tuple[1] < 2500]
print(endangered)

Output:
['black rhino', 'orangutan', 'sumatran elephant', 'blue whale', 'giant panda', 'green turtle']

Result	Actual Value	Expected Value	Notes
Pass	"[('go...000)]"	"[('go...000)]"	Testing that pop_info was created correctly.
Pass	'map('	'\nspec...ed)\n\n'	Testing your code (Don't worry about actual and expected values).
Pass	'filter('	'\nspec...ed)\n\n'	Testing your code (Don't worry about actual and expected values).
Pass	'sum('	'\nspec...ed)\n\n'	Testing your code (Don't worry about actual and expected values).
Pass	'zip('	'\nspec...ed)\n\n'	Testing your code (Don't worry about actual and expected values).
Pass	"['bla...tle']"	"['bla...tle']"	Testing that endangered was created correctly.
You passed: 100.0% of the tests



