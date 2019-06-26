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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
