FILES:
//The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
with open('travel_plans.txt') as f:
    text = f.read() # list of lines
    num = sum(len(line) for line in text) # sum up the length of each line
print(num)

//We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
with open('emotion_words.txt') as f:
  text = f.read().splitlines() # list of lines
num_words = sum(len(line.split()) for line in text) # split each line on spaces, sum up the lengths of the lists of words
print(num_words)

//Assign to the variable num_lines the number of lines in the file school_prompt.txt.
with open('school_prompt.txt') as f:
  text = f.read().splitlines() # list of lines
num_lines = len(text) # length of the list = number of lines
print(num_lines)

//Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
with open('school_prompt.txt') as f:
    beginning_chars = f.read()[:30]

//Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
with open('travel_plans.txt') as f:
    first_chars = f.read()[:33]
    
//Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
schoolfile = open("school_prompt.txt","r")
word_list = schoolfile.read().split()
print(word_list)
p_words = []
for word in word_list:
    if "p" in word:
         p_words.append(word)
print(p_words)

//Create a list called emotions that contains the first word of every line in emotion_words.txt
# open the file.
with open("emotion_words.txt") as f:
# Read the while file content as string
   filecontent = f.read()
   print(filecontent)
# Split the filecontent string to lines.
   lines = filecontent.splitlines(False)
   print(lines)
# Hold the emotions - The first word in each line of the given file.
   emotions = []
# Iterate through the lines
   for line in lines:
# Split the line to words by space
        words = line.split(' ')
# Task the first word
        firstWord = words[0]
# Add the emotion
        emotions.append(firstWord)
# Print the emotions
   print(emotions)
    
   //Using the iterator variable and while loop
#   emotions = []
    # Iterate through the lines
#   currentLineNo = 0
#   while currentLineNo < len(lines):
       # Split the line to words by space
#       line = lines[currentLineNo]
#       words = line.split(' ')
       # Task the first word
#       firstWord = words[0]
       # Add the emotion
#       emotions.append(firstWord)
#       currentLineNo+=1

Output:
Sad upset blue down melancholy somber bitter troubled
Angry mad enraged irate irritable wrathful outraged infuriated
Happy cheerful content elated joyous delighted lively glad
Confused disoriented puzzled perplexed dazed befuddled
Excited eager thrilled delighted
Scared afraid fearful panicked terrified petrified startled
Nervous anxious jittery jumpy tense uneasy apprehensive

['Sad upset blue down melancholy somber bitter troubled', 'Angry mad enraged irate irritable wrathful outraged infuriated', 'Happy cheerful content elated joyous delighted lively glad', 'Confused disoriented puzzled perplexed dazed befuddled', 'Excited eager thrilled delighted', 'Scared afraid fearful panicked terrified petrified startled', 'Nervous anxious jittery jumpy tense uneasy apprehensive']
['Sad', 'Angry', 'Happy', 'Confused', 'Excited', 'Scared', 'Nervous']

// Using the file school_prompt.txt, assign the third word of every line to a list called three.
# open the file.
with open("school_prompt.txt") as f:
# Read the while file content as string
   filecontent = f.read()
   print(filecontent)
# Split the filecontent string to lines.
   lines = filecontent.splitlines(False)
   print(lines)
# Hold the third word - The third workd in each line of the given file.
   three = []
# Iterate through the lines
   for line in lines:
# Split the line to words by space
        words = line.split(' ')
# Task the third word
        thirdWord = words[2]
# Add the third word
        three.append(thirdWord)
# Print the third word
   print(three)
   
Output:
Writing essays for school can be difficult but
many students find that by researching their topic that they
have more to say and are better informed. Here are the university
we require many undergraduate students to take a first year writing requirement
so that they can
have a solid foundation for their writing skills. This comes
in handy for many students.
Different schools have different requirements, but everyone uses
writing at some point in their academic career, be it essays, research papers,
technical write ups, or scripts.

['Writing essays for school can be difficult but', 'many students find that by researching their topic that they', 'have more to say and are better informed. Here are the university', 'we require many undergraduate students to take a first year writing requirement', 'so that they can', 'have a solid foundation for their writing skills. This comes', 'in handy for many students.', 'Different schools have different requirements, but everyone uses', 'writing at some point in their academic career, be it essays, research papers,', 'technical write ups, or scripts.']
['for', 'find', 'to', 'many', 'they', 'solid', 'for', 'have', 'some', 'ups,']



DICTIONARIES: Unordered,bag of key value pairs.
//At the halfway point during the Rio Olympics, the United States had 70 medals, Great Britain had 38 medals, China had 45 medals, Russia had 30 medals, and Germany had 17 medals. Create a dictionary assigned to the variable medal_count with the country names as the keys and the number of medals the country had as each key’s value.
medal_count = {}
medal_count['United States'] = 70
#medal_count = { "United States" : 70}
medal_count['Great Britain'] = 38
medal_count['China'] = 45
medal_count['Russia'] = 30
medal_count['Germany'] = 17
print(medal_count)
output:
{'China': 45, 'Great Britain': 38, 'Russia': 30, 'Germany': 17, 'United States': 70}


//Given the dictionary swimmers, add an additional key-value pair to the dictionary with "Phelps" as the key and the integer 23 as the value. Do not rewrite the entire dictionary.
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}
swimmers['Phelps'] = 23

//Add the string “hockey” as a key to the dictionary sports_periods and assign it the value of 3. Do not rewrite the entire dictionary.
sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}
sports_periods['hockey'] = 3


//The dictionary golds contains information about how many gold medals each country won in the 2016 Olympics. But today, Spain won 2 more gold medals. Update golds to reflect this information.
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}

golds['Spain'] = golds['Spain'] + 2


//Dictionary Methods:
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
for key in golds.keys():
    print(key,"has the value",golds[key])
    
//Call List function to get list
keys = list(golds.keys())
print(keys)

//#tuples 
print(list(golds.values()))
#Tuples
print(list(golds.items()))

output:
Italy has the value 12
USA has the value 33
Brazil has the value 15
China has the value 27
Spain has the value 19
Canada has the value 22
Argentina has the value 8
England has the value 29
['Italy', 'USA', 'Brazil', 'China', 'Spain', 'Canada', 'Argentina', 'England']

[12, 33, 15, 27, 19, 22, 8, 29]
[('Italy', 12), ('USA', 33), ('Brazil', 15), ('China', 27), ('Spain', 19), ('Canada', 22), ('Argentina', 8), ('England', 29)]

//Create a list of the countries that are in the dictionary golds, and assign that list to the variable name countries. Do not hard code this.
countries = list(golds.keys())
print(countries)
output:
['Italy', 'USA', 'Brazil', 'China', 'Spain', 'Canada', 'Argentina', 'England']

//Provided is the dictionary, medal_count, which lists countries and their respective medal count at the halfway point in the 2016 Rio Olympics. Using dictionary mechanics, assign the medal count value for "Belarus" to the variable belarus
medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}
belarus = medal_count.get("Belarus")
print(belarus)

//The dictionary total_golds contains the total number of gold medals that countries have won over the course of history. Use dictionary mechanics to find the number of golds Chile has won, and assign that number to the variable name chile_golds
total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87, "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22, "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}
chile_golds = total_golds.get("Chile")

//Provided is a dictionary called US_medals which has the first 70 metals that the United States has won in 2016, and in which category they have won it in. Using dictionary mechanics, assign the value of the key "Fencing" to a variable fencing_value. Remember, do not hard code this.
US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, "Golf": 1, "Weightlifting": 1}
fencing_value = US_medals.get("Fencing")


//Dictionary Accumulators
//The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for value in Junior:
    credits = credits +Junior[value] 
print(credits)

//Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for character in str1:
    if character not in freq:
        freq[character] = 0
    freq[character] = freq[character] + 1
print(freq)
{'p': 9, 'e': 8, 't': 1, 'r': 3, ' ': 7, 'i': 3, 'c': 3, 'k': 3, 'd': 2, 'a': 1, 'o': 1, 'f': 1, 'l': 1, 's': 1}

//Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
s1 = "hello"
counts = {}
for letter in s1:
    if letter not in counts:
        counts[letter] = 0
    counts[letter] = counts[letter] + 1
print(counts)
{'e': 1, 'o': 1, 'l': 2, 'h': 1}


//Create a dictionary, freq_words, that displays each word in string str1 as the key and its frequency as the value.
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
str1 = str1.split()
print(str1)
freq_words = {}
for word in str1:
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] = freq_words[word] + 1
print(freq_words)
['I', 'wish', 'I', 'wish', 'with', 'all', 'my', 'heart', 'to', 'fly', 'with', 'dragons', 'in', 'a', 'land', 'apart']
{'a': 1, 'I': 2, 'wish': 2, 'with': 2, 'all': 1, 'my': 1, 'heart': 1, 'to': 1, 'fly': 1, 'dragons': 1, 'in': 1, 'land': 1, 'apart': 1}


//Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
sent = sent.split()
print(sent)
wrd_d = {}
for word in sent:
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] = wrd_d[word] + 1
print(wrd_d)
['Singing', 'in', 'the', 'rain', 'and', 'playing', 'in', 'the', 'rain', 'are', 'two', 'entirely', 'different', 'situations', 'but', 'both', 'can', 'be', 'good']
{'in': 2, 'Singing': 1, 'the': 2, 'rain': 2, 'and': 1, 'playing': 1, 'are': 1, 'two': 1, 'entirely': 1, 'different': 1, 'situations': 1, 'but': 1, 'both': 1, 'can': 1, 'be': 1, 'good': 1}


//Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char
sally = "sally sells sea shells by the sea shore"

characters = {}

for letter in sally:
    if letter not in characters:
        characters[letter] = 0
    characters[letter] = characters[letter] + 1
print(characters)

best_char = 0
highest_occurrence = 0
for item in characters.items():
    if (item[1] > highest_occurrence):
        highest_occurrence=item[1]
        best_char=item[0]
print(best_char)  

"""
best_char = 0
highest_occurrence = 0
#iterate through key in characters dictionary
for currentKey in characters:
    # Get the value for the current key
    valueForCurrentKey = characters[currentKey]
    #compare key value to highest occurance
    if (valueForCurrentKey > highest_occurrence):
        highest_occurrence = valueForCurrentKey
        best_char = currentKey
print(best_char)    
"""
{'e': 6, 't': 1, 'r': 1, ' ': 7, 'a': 3, 'o': 1, 'l': 6, 's': 8, 'h': 3, 'y': 2, 'b': 1}
s

//Do the same as above but now find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char
sally = "sally sells sea shells by the sea shore and by the road"
characters = {}

for letter in sally:
    if letter not in characters:
        characters[letter] = 0
    characters[letter] = characters[letter] + 1
print(characters)

worst_char = 0
lowest_occurrence = None
#iterate through key in characters dictionary
for currentKey in characters:
    # Get the value for the current key
    valueForCurrentKey = characters[currentKey]
    #compare key value to lowest occurance
    if if (lowest_occurrence == None or lowest_occurrence > valueForCurrentKey) :
        lowest_occurrence = valueForCurrentKey
        worst_char = currentKey
print(worst_char)

{'e': 7, 't': 2, 'r': 2, ' ': 11, 'd': 2, 'a': 5, 'o': 2, 'l': 6, 's': 8, 'h': 4, 'y': 3, 'b': 2, 'n': 1}
n

//Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string1 = string1.lower()
letter_counts = {}
for character in string1:
    if character not in letter_counts:
        letter_counts[character] = 0
    letter_counts[character] = letter_counts[character] + 1
print(letter_counts)

{'e': 29, 't': 19, 'r': 12, ' ': 53, 'i': 14, 'c': 3, 'k': 2, 'd': 7, 'a': 17, 'o': 17, 'f': 9, 'l': 11, 's': 15, 'h': 11, 'y': 1, 'b': 1, 'n': 15, 'm': 4, ',': 4, 'u': 8, '.': 4, 'v': 3, 'g': 1, 'w': 6}

//Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
p = p.lower()
low_d = {}
for character in p:
    if character not in low_d:
        low_d[character] = 0
    low_d[character] = low_d[character] + 1
print(low_d)

{'e': 12, 't': 9, 'r': 3, ' ': 20, 'i': 3, 'c': 2, 'd': 1, 'a': 6, 'o': 8, 'f': 3, 'l': 1, 's': 5, 'h': 6, 'y': 1, 'b': 2, 'n': 1, 'm': 3, 'u': 7, '.': 2, 'v': 1, 'g': 3}
