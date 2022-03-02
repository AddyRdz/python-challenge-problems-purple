# Problems Completed [ ]

# Your test/solution code here 
from cmath import nan
from operator import truediv


def even_range(start,end):
    even_range=[]
    if (start%2!=0):
        start=start+1
    for num in range(start,end,2):
        even_range.append(num)
    return even_range
print(even_range(4,11))

# Problem 0
def phrase_finder(words,phrase):
    phrase_split = phrase.split()
    print(phrase_split)
    counter = 0
    for w in words:
        for p in phrase_split:
            if w ==p:
                counter +=1
    if counter ==2:
        return True
    else:
        return False
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world'))
# Problem 1
def hammingDistance(string1,string2):
    c = 0
    if len(string1) != len(string2):
        return 'NaN'
    elif string1 == string2:
        return 0
    else:
        for s in range(len(string1)):
            if string1[s] != string2[s]:
                c += 1 
    return c    
print(hammingDistance('!!!!', '****'))
    
    
# Problem 2

# Problem 3


