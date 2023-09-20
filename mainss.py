"""
def hide_mail(get):
    result = ""
    for i,mail in enumerate(get):
        if i > get.find("@") and i < get.find("."):
            result += "*"
        else:
            result += get[i]
    print(result)

hide_mail("jeevasdckap@gmail.com")
"""

# def hide_mail(user_input):
#     output = ""
#     for i,value in enumerate(user_input):
#         if user_input[i] == "@" and user_input[i] == ".":
#             output
#
# hide_mail("jasmine@gmail.com")

# Udacity python
# arithmetic operation
"""
+ addition (add two numbers) 8+9
- subtract (subtract two numbers) 4-1
* multiplication (multiply numbers) 4*7
/ division (give round number) 5 / 2 = 2
% mod (give reminder) 5 / 2 = 5
** exponentiation (give power number) 2 ** 3 = 8

"""

# Integers and Float
"""
x = 3 # integer
y = 3.5 # float

"""

# python indentation - dont give some space unwanted place like this
"""
print(3 + 1) #correct
print(   3 + 1   ) # wrong it give answer but its not right
"""

# Comparison operators and logical operators
"""
a = 43 > 2 # it return boolean value true because 43 is greater than 2

b = 34 > 2 and 54 < 2 # it gives return false because and operator check two conditions 54 isn't less than 2
c = 34 > 2 or 54 < 2 # it check only one condition 34 is greater than 2 
"""

# strings
"""
string = "jeeva\'s is my friend" # you can use \ for single and double codes problem
new_line = "jeva\n jas" # go new line
tab = "jeeva \t jas" # give some space
"""

# string concentation
"""
name1 = "jeeva"
name2 = "jasmine"

name3 = name1 + name2
"""

# multiply string
"""
value = 3 * "jas" # print three time jas
"""

# type and type conversion
"""
print(type(4)) # int
print(type(4.3)) # float
print(type("jeeva")) # string
"""

# string in-build methods
"""
print(len("jeeva")) # give a lenght of string
print("jeeva".upper())
print("jEeva".lower())
print("jeeva".find("j")) # it gives the index of search string
"""

# string concatenation four methods

"""
# string concatenation
print("jeeva" + "jas") # string concatenation only concat a string not a number

# % operator -- you can add variable inside the string and also add multiple variable inside a sring using this method

d = "jeeva" # use %s to add string
e = 4 # use %d to add a number
g = "jasmine"
f = "%s got %d score" % (d,e) # you can put variable end the line and apply order
print(f)

# format method
h = "hi, {} you got score {}".format(d,e) # you can use {} to add a variable on string
second_method = "hi, {1} you got score {0}".format(d,e) # you can also positioned to add a string
third_method = "hi {score} you got score {name}".format(name=d,score=e) # you can also give a name on args and add a string
print(third_method)

# f-string method
print(f"{d} got score {e}") # you should put f letter on front of the string and add a variable name inside the carle bracket
"""


# DATA STRUCTURE
# list and membership operations
"""
names = [1,2,3,4,5,6,7,8,9]
print(names[0]) # give 0 index value
print(names[-1]) # give last value
# print(names[32]) # give an error "out of range"

slice_names = names[len(names)::-1] # [start:end:step]
"""

# list methods
"""
# join
string = "Jas".join(["1","2","3"]) # --without affect last element, insert value between two elements
print(string)

# append()
lists = [1,2,3,4]
lists.append(5) # add last of the element
print(lists)
"""

# Tuples -- immutable ordered sequences of elements --tuples cannot be changed --tuples are more memory efficient
"""
dimensions = (52, 40, 100)
print("the dimensions are {} x {} x {}".format(dimensions[0],dimensions[1],dimensions[2]))
"""

# sets
"""
--unorder collections of unique elements
--using carle brackets
--it cannot be access using index
--you can able to add and remove element
"""
"""
fruit = {"apple", "banana", "orange", "grapefruit"}
fruit.add("grape") # add element
fruit.pop() # remove element randomly
print(fruit)
"""

# dictionary
"""
--mutable data type 
--storing mapping of unique key to values
"""

"""
sets = {
    "name":"jeeva",
    "age":20,
    "clg":"cpt",
    "village":{
        "village":"veerapandi",
        "dist":"villupuram",
        "tk":"kandachipuram"
    }
}

# accessing elements
single_value = sets["name"] # access element using key
nested_value = sets["village"]["dist"] # access nested element using [][]

# assign elements
one_value = sets["name"] = "jas"
nested = sets["village"]["dist"] = "vilupuram"

# sets in-build methods

# len --give length
print(len(sets["village"])) # print length of the sets

# in --return boolean value here or not key
print("clg" in sets)

# sort
sorted_keys = sorted(sets.keys()) # sorted key alphabatic
print(max(sorted_keys)) # give maximum length of the key
"""

# If statements


if 2 > 1:
    print("crt")
else:
    print("wrong")