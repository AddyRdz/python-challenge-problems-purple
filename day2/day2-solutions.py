# Problems Completed [ ]

# Your test/solution code here 
def reverseString(string):
    string2 = string.replace('-', ' ').split(' ')
    string2.reverse()
    string2 = '-'.join(string2)
    return string2
# print(reverseString("Go-to-the-store"))

# Problem 0
def is_element(arr, ele):
    counter = 0
    for l in range(len(arr)):
        if ele == arr[l]:
            var = l
        else:
            counter +=1
            if counter == len(arr):
                var = False
    return var
print(is_element(["a","b","c"], "a"))

# Problem 1
def merge_dictionaries(d1,d2):
    d1.update(d2)
    return d1
print(merge_dictionaries({"a": 1, "b": 2, "c": 3}, {"d": 4}))

# Problem 2

# Problem 3


