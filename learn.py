# Name = "jeeva"
#
# para = " My name is jeeva"
#
# # length --print string length
# print(len(Name))
#
# # strip --removing front and backspace
# print(para.strip())
#
# # uppercase
# print(Name.upper())
# # lower
# print(Name.lower())
#
# # replace a word
# print(Name.replace("j", "jas"))
#
# # split
# print(Name.split("v"))
#
# # check word is here
# print("je" in Name)
#
# # concat a string
# a = "jeeva "
# b = "jasmine"
# print(a + b)

# # casting int, float, str
# number = 44
# print(int(number))
#
# # gettype
# print(type(number))


# # list same as string --you can customize this element
# loves = ["maha", 'jas', 'priya', "maha"]
# loves[1] = "srija"
# print("srija" in loves)
# print(loves[1])
# print(len(loves))
# loves.append("figure")
# print(loves)
#
#
# number = [4, 2, 5, 6]
# number.sort()
# number.sort(reverse=True)
# print(number)
#
# add = loves + number
#
# print(add)

# #tupils --you can't change this element
# name = ("jas", "srija")
# number = (4, 6, 7)
# add = name + number
#
# print(add)

# # set --no index number --it prints randomly
#
# fruits = {"maha", "srija"}
# fruits.add("priya")
# print(fruits)

# Dictionary

# Calculator

"""

input1 = int(input("enter yout number one"))
input2 = int(input("enter your number two"))
operator = input("enter your operator")


def calculator(num1, num2, symbol):
    if symbol == "+":
        return num1 + num2
    elif symbol == "-":
        return num1 - num2
    elif symbol == "*":
        return num1 * num2
    elif symbol == "/":
        return num1 / num2
    else:
        return "Please enter correct input"


print(calculator(input1, input2, operator))

"""

# reverse string
"""
user_input = "racecar"
output = ""

def palindrome(get_input, result):
    for i in range(len(get_input) - 1, -1, -1):
        result += get_input[i]
    if get_input == result:
        print("it is palindrome")
    else:
        print("it is not palindrome")


palindrome(user_input, output)

"""


# capitalize
"""

def capitalize(lower_name):
    res = ""
    for i in range(0, len(lower_name)):
        if i % 2 != 0:
            res += lower_name[i].upper()
        else:
            res += lower_name[i]
    return res


print(capitalize("jasmine"))

"""
