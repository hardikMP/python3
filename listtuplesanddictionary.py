# Lists and corresponding functions
# Lists are basically arrays in C but the only difference is that it can have different data types of values in storage
list = [10, 20, 30, "Hardik"] #Creates a new list with values 10,20,30 and John
tinyList = [70]

print(list) #Prints the complete list
print(list[3]) #Prints value at the 3rd index. Remeber index starts at 0
print(list[2:]) #Prints values starting from 2nd index til the end of the list
print(list * 2) #Prints the list n number of times. In this case n = 2
print(list + tinyList) #Prints the merged list of values of tinyList appened after the list values

#Tuple are mostly like lists with few differences such as tuple's value can not be changed
#Also tuples can only be created if there are more than one value otherwise it is treated as a variable
tuple = (40, 50, 60, "Prajapati")
tinyTuple = (80, 90)

print (tuple)           # Prints the complete tuple
print (tuple[3])        # Prints 3rd element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinyTuple * 2)   # Prints the merged Tuple of values of tinyTuple appened after the Tuple values
print (tuple + tinyTuple) # Prints concatenated tuple

# Dictionaries are like associative arrays and use hashtable structure with key and value pair
dictionary = {"hardik" : 9820276067, "Nitin" : 9699678658}
print(dictionary) # Prints the complete dictionary
print(dictionary["hardik"]) #Prints the value of key "hardik"
print(dictionary.keys()) # Prints all the keys of dictionary
print(dictionary.values()) # Prints all the values of dictionary

# You cant concatenate a tuple with just one value in it to anothe tuple
# You cant change the value of any tuple index

# You cant concatenate list and tuples together 
# print(list + tuples)