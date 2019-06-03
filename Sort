//Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted("alwnfiwaksuezlaeiajsdl")
print(sorted(sorted_letters,reverse = True))
sorted_letters = sorted(sorted_letters,reverse = True)

Output : ['z', 'w', 'w', 'u', 's', 's', 'n', 'l', 'l', 'l', 'k', 'j', 'i', 'i', 'f', 'e', 'e', 'd', 'a', 'a', 'a', 'a']
Result	Actual Value	Expected Value	Notes
Pass	"['z',... 'a']"	"['z',... 'a']"	Testing that sorted_letters has the correct value.
You passed: 100.0% of the tests

//Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.
animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)
print(animals_sorted)

Output:
['antelope', 'bear', 'cat', 'cow', 'deer', 'elephant', 'elk', 'giraffe', 'goat', 'minx', 'moose', 'otter', 'rabbit', 'salamander', 'tiger', 'yak', 'zebra']

Result	Actual Value	Expected Value	Notes
Pass	"['ant...bra']"	"['ant...bra']"	Testing that animals_sorted was created correctly.
You passed: 100.0% of the tests


//The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

alphabetical = sorted(medals.keys())
print(alphabetical)
output :
['China', 'Germany', 'Japan', 'Russia', 'South Korea', 'United States']
Result	Actual Value	Expected Value	Notes
Pass	"['Chi...tes']"	"['Chi...tes']"	Testing that alphabetical value is assigned to correct values.
You passed: 100.0% of the tests


//Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

top_three = sorted(medals.keys(), key = lambda k: medals[k],reverse = True)[:3]
print(top_three)
output : ['United States', 'China', 'Russia']
Result	Actual Value	Expected Value	Notes
Pass	"['Uni...sia']"	"['Uni...sia']"	Testing that top_three value is assigned to correct values.
You passed: 100.0% of the tests


//We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

most_needed = sorted(groceries.keys(), key = lambda k: groceries[k], reverse = True)

output : ['granola bars', 'carrots', 'spinach', 'bananas', 'onions', 'coffee', 'apples', 'cereal', 'salsa', 'pasta', 'peanut butter', 'orange juice', 'rice', 'popcorn']
Result	Actual Value	Expected Value	Notes
Pass	"['gra...orn']"	"['gra...orn']"	Testing that most_needed was created correctly.
You passed: 100.0% of the tests



//Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
def last_four(x):
    return str(x)[-4:]     

sorted_ids = sorted(ids, key=lambda x: str(x)[-4:])

output : [17570002, 17572342, 17572345, 17573005, 17579000, 17579329]
Result	Actual Value	Expected Value	Notes
Pass	'[1757...9329]'	'[1757...9329]'	Testing that sorted_ids is assigned to correct values.
You passed: 100.0% of the tests


//Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted(ids, key=lambda x: str(x)[-4:])
print(sorted_id)

Output : [17570002, 17572342, 17572345, 17573005, 17579000, 17579329]
Result	Actual Value	Expected Value	Notes
Pass	'[1757...9329]'	'[1757...9329]'	Testing that sorted_id is assigned to correct value.
Pass	'lambda'	'\nids ...d_id)'	Testing your code (Don't worry about actual and expected values).
You passed: 100.0% of the tests


//Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, key=lambda x: str(x)[1:])
print(lambda_sort)

Output : ['dance', 'zebra', 'hi', 'how are you', 'apple', 'bye']
Result	Actual Value	Expected Value	Notes
Pass	"['dan...bye']"	"['dan...bye']"	Testing that lambda_sort has the correct value.
Pass	'lambda'	'\nex_l...sort)'	Testing your code (Don't worry about actual and expected values).
You passed: 100.0% of the tests









