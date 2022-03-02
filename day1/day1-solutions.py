# Problems Completed [ ]

# Your test/solution code here 
from cmath import nan


def even_range(start,end):
    even_range=[]
    if (start%2!=0):
        start=start+1
    for num in range(start,end,2):
        even_range.append(num)
    return even_range
print(even_range(4,11))

# Problem 0

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


