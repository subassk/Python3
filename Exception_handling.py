//The code below takes the list of country, country, and searches to see if it is in the dictionary gold which shows some countries who won gold during the Olympics. However, this code currently does not work. Correctly add try/except clause in the code so that it will correctly populate the list, country_gold, with either the number of golds won or the string “Did not get gold”.

gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []

for x in country:
    try:
        country_gold.append(gold[x])
    except:
        country_gold.append("Did not get gold")

print(country_gold)

[1, 'Did not get gold', 'Did not get gold', 10, 'Did not get gold', 46]

Result	Actual Value	Expected Value	Notes
Pass	"[1, '..., 46]"	"[1, '..., 46]"	Testing that country_gold is assigned to correct values
You passed: 100.0% of the tests

    
 //Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes.   
     
di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except:
        print("Total number of puppies:", total)


Total number of puppies: 40
    
Result	Actual Value	Expected Value	Notes
Pass	130	130	Testing that total has the correct value.
You passed: 100.0% of the tests    
    
    
//The list, numb, contains integers. Write code that populates the list remainder with the remainder of 36 divided by each number in numb. For example, the first element should be 0, because 36/6 has no remainder. If there is an error, have the string “Error” appear in the remainder.
    
numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainder = []

for num in numb:
    try:
        currentRemainder = 36 % num
        remainder.append(currentRemainder)
    except:
        remainder.append("Error")
print(remainder)    
    
[0, 'Error', 0, 4, 0, 0, 'Error', 0, 36, 'Error', 36, 'Error', 0, 13]

Result	Actual Value	Expected Value	Notes
Pass	"[0, '..., 13]"	"[0, '..., 13]"	Testing that remainder is assigned to correct values.
You passed: 100.0% of the tests    
    
    
//Provided is buggy code, insert a try/except so that the code passes.
    
lst = [2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,465,56,7,3,43,23]

lst_three = []

for num in lst:
    try:
        if 3 % num == 0:
            lst_three.append(num)
            print("This is the List",lst_three)
    except:
        print("something went wrong",lst_three)
            
    
 something went wrong []
something went wrong []
This is the List [1]
This is the List [1, 3]

Result	Actual Value	Expected Value	Notes
Pass	[1, 3]	[1, 3]	Testing that lst_three has the correct values.
You passed: 100.0% of the tests
    
    
// Write code so that the buggy code provided works using a try/except. When the codes does not work in the try, have it append to the list attempt the string “Error”.   
    
 full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

attempt = []

for elem in full_lst:
    try:
        attempt.append(elem[1])
        print(attempt)
    except:
        attempt.append("Error")   
    
    
['b']
['b', 'd']
['b', 'd', 'g']
['b', 'd', 'g', 'Error', 'k']
['b', 'd', 'g', 'Error', 'k', 'o']
['b', 'd', 'g', 'Error', 'k', 'o', 'r']
['b', 'd', 'g', 'Error', 'k', 'o', 'r', 'Error', 'v']
['b', 'd', 'g', 'Error', 'k', 'o', 'r', 'Error', 'v', 'x']    
    
    
 Result	Actual Value	Expected Value	Notes
Pass	"['b',...ror']"	"['b',...ror']"	Testing that attempt has the correct values.
You passed: 100.0% of the tests   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
