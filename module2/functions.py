"""
write a fuction that check number of chars in a string 
return number of chars
"""
def number_of_chars(x):
    #chack if variable is string or int
     print("x is string")
     for i in x:
        return len(x)
     
    

# function call
#print(number_of_chars('rose'))

def my_list():
    #liist declaration
    list1 = [1, 2, 3, 10, 5, 20, 0]
    list2 = ['Rose', 'a', 'line']
    list3 = ['Rose', 12, True, 10.2]

    #print everything in my list
    print(*list1)
    #print the way it is displayed
    print(list3, sep= " ")

    #adding something into the list
    list1.insert(len(list1), -2)
    print(list1)
    # using apend 
    list2.append(7)
    print(list2)
    #using extend
    list1.extend(['ROSELINE', 1, False])
    print(list1)

    ## remove something from the list
    # using pop
    list1.pop(2)
    print(list1)
    list1.pop()
    print(list1)
    # using del
    del list1[0]
    print(list1)
    
    # iterate through a list
    for x in list1:
        print(x)
# my_list()
# working with tuples
# declare a tuple
def my_tuple():
    tuple1 = ('Rose', 1, True, 12,5, 'Rose')
    tuple2 = 1, 12,5, 3, False, 'lynne'
    #check type
    print(type(tuple2))
    # counting number of occurance
    print(tuple1.count('Rose'))
    # get the index
    print(tuple2.index('lynne'))

    # iterate through the values and print them out
    for y in tuple1:
        print(y)

#my_tuple()
# working with sets
def my_set():
    set1 = {1, 2, 3, 4, 5, 10, 11, }
    print(set1)
    # add iterm in a set
    set1.add(7)
    print(set1)
    #remove a number in a set
    set1.remove(1)
    print(set1)
    set1.discard(2)
    print(set1)
    set2 = {6, 8, 9, 10, 11}
    # get elements in 1 and not in 2
    print(set1.difference(set2))
    print(set1 - set2)
    #symentrical differents get elements in  1and not in 2
    print(set1.symmetric_difference(set2))
    print(set1 ^ set2)
    # to join set together 
    print(set1.union(set2))
    print(set1 | set2)
    # using intersecion to get all elements in 1 and 2
    print(set1.intersection(set2))
    print(set1 & set2)
#my_set()
    
# working with dictionaries
def dictionaries():
    dict1 = { } 
    print(type(dict1))
    #adding values in my dict
    dict1 = {1: 'Rose', 'Name': 1}
    print(dict1)
    #access value in dict
    print(dict1[1])
    # add new item to dict
    dict1[2] = 'Lynne'
    print(dict1)
    # update  the key
    dict1[1] = 'ROSELINE'
    print(dict1)
    # to delete
    del dict1['Name']
    print(dict1)
    # to iterate and print keys only
    for x in dict1:
        print(x)

    # to iterate and print both keys and values
    for key, value in dict1.items():
        print(str(key) + " : " + value)  
#dictionaries() 

#  args
def key_word_args(*args):
    #args  allow any number of ags to be passed to my fuction
    sum = 0
    for x in args:
         sum += x
    return sum
#print(key_word_args(1, 2, 7, 13, 5, 8))

# using kwargs
def keyword_args(**kwargs):
    #pass any amount of keyword args
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return round(sum, 2)
print(keyword_args(cofee=2.99, cake=5.00, juice=2.50))