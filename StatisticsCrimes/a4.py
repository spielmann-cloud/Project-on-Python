"""
@author: sarvar umurzakov
"""

""" Importing os module to correct indicacte the path """
import os

""" function read_stats takes filename as argument and returns list of crimes """
def read_stats(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(folder, filename)

    listOfCrimes = []
    with open(filename, "r") as file:
        line = file.readline()
        while(line != ""):
            line = line.strip()
            listOfCrimes.append(line.split(","))
            line = file.readline()
    listOfCrimes.pop(0)
    return listOfCrimes

""" function read_codes takes filname as argument and returns dictionary, where key is cods and value is type of crime """
def read_codes(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(folder, filename)
    myList = []

    with open(filename, "r") as file:
        line = file.readline()
        myList = line.strip().split(",")
        myList[0] = myList[0][1:]
        myList[-1] = myList[-1][:-1]
        myList = [val.strip().split(":") for val in myList]
    return dict(myList)

""" function crimes_by_code takes code and dict as arguments and returns list of crimes by certain code in dictionary """
def crimes_by_code(code, dict):
    return [val for val in read_stats("crime_in_vancouver.csv") if val[0] == dict[str(code)]]

""" function sort_by_years takes stats as list and returns a copy of sorted stats by years. Sorting method ist HeapSort 
For this purpose two methods - heapIt, heapSort - was added.
"""
def sort_by_years(stats):
    myList = stats[:]
    heapSort(myList)
    return myList

""" function heapIt takes array, size of heap and root as arguments and bring array to correct heap tree """
def heapIt(array, heapSize, root):
    maximum = root
    left_child = root * 2 + 1
    right_child = root * 2 + 2

    if(left_child < heapSize and int(array[left_child][1]) < int(array[maximum][1])):
        maximum = left_child

    if(right_child < heapSize and int(array[right_child][1] ) < int(array[maximum][1])):
        maximum = right_child

    if(maximum != root):
        tmp = array[root]
        array[root] = array[maximum]
        array[maximum] = tmp
        heapIt(array, heapSize, maximum)

""" function heapSort takes array as argument and sort array using heapIt function """
def heapSort(array):
    size = len(array)

    for i in range(size, -1, -1):
        heapIt(array, size, i)

    for i in range(size - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapIt(array, i, 0)


""" function filter_crime_stats takes stats, param, x, y as arguments and returns list of crimes with start time as x 
and end time as y. By invalid parameter returns a message, otherwise list"""
def filter_crime_stats(stats, param, x, y):
    switcher = {
        "year":1,
        "month":2,
        "day":3
    }
    if(str(param).lower().strip() not in switcher.keys()):
        return "Invalid parameter"

    index = switcher[param.lower()]
    return [[val[0], val[1], val[2], val[3], val[7]] for val in stats if int(val[index]) in range(x,y+1)]

""" function code_from_keywords takes keywords, dict as arguments and returns list of all crime codes """
def code_from_keywords(keywords, dict):
    results = []

    for element in keywords:
        for key, value in dict.items():
            if(value.lower().find(element) != -1):
                results.append(key)
    return results

""" function crime_by_location takes stats as list and returns list of all crimes that occurred in x±1000 and y±1000
Function asks user to enter appropriate values for x and y, otherwise exception will be thrown.
"""
def crime_by_location(stats):
    while(True):
      try:
        print("Enter the x and y-coordinates of the search location.")
        x = int(input("Enter an x coordinate between 490001 and 511175. > "))
        y = int(input("Enter a y coordinate between 5000024 and 5462059. >"))
        if(x < 490001 or x > 511175 or y < 5000024 or y > 5462059):
            raise Exception
        return [val for val in stats if int(val[8]) in range(x-1000, x+1001) and int(val[9]) in range(y-1000, y+1001)]
      except:
        print("Invalid values, please try again")
        continue

""" function code_and_freq takes stats and dict as arguments and returns new dictionary with key - code and 
    value - list, where first element is frequency and second is type """
def code_and_freq(stats, dict):
    return {key:[len(crimes_by_code(key, dict)), value] for key,value in dict.items()}



""" Checking our functions """
list_of_crimes = read_stats('crime_in_vancouver.csv')
print(list_of_crimes)
print("*" * 20)

codes_and_crimes = read_codes("crime_codes.json")

print(crimes_by_code(110, codes_and_crimes))
print("*" * 20)


print(sort_by_years(list_of_crimes))
print("*" * 20)


print(filter_crime_stats(list_of_crimes,'year',2007,2008))
print("*" * 20)

print(code_from_keywords(['break','homicide'],codes_and_crimes))
print("*" * 20)

crime_by_location(list_of_crimes)
print("*" * 20)

code_and_freq(list_of_crimes,codes_and_crimes)


