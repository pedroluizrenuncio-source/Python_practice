import math

#region Exercise 1. For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# def square_digits(num):
#     new_number = ''
#     for element in str(num):
#         new_number += str(int(element)**2)
#     return new_number

# print(square_digits(220384))
# endregion
# region Exercise 2 01.06.2026
#2. # Complete the function which will return the area of a circle with the given radius.

# Returned value is expected to be accurate up to tolerance of 0.01.

# If the radius is not positive, raise ValueError.

# Example:

# circle_area(43.2673)      # returns 5881.248  (± 0.01)
# circle_area(68)           # returns 14526.724 (± 0.01)
# circle_area(0)            # raises ValueError
# circle_area(-1)           # raises ValueError
#

# def circle_area(r):
#     if r <= 0:
#         raise ValueError("Radius must be positive")
    
#     area = math.pi * r ** 2
#     return round(area, 2)

# print(circle_area(43.2673))  # 5881.25
# endregion
#region Exercise 3 01.06.2026 
#3. ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# !def validate_pin(pin):
#     if len(pin) in [4, 6] and pin.isdigit():
#         return True
#     else:
#         return False
    
# print(validate_pin("123456"))
# endregion
#region Exercise 4(02/06/2026)
# A square of squares
# You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

# However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

# Task
# Given an integral number, determine
#  if it's a square number:

# In mathematics, a square number
#  or perfect square is an integer
#  that is the square of an integer; in
#  other words, it is the product of some 
# integer with itself.

# The tests will always use some
#  integral number, so don't worry about
#  that in dynamic typed languages.

# Examples
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false
  

# def is_square(n):    
#     if n < 0:
#         return False
#     else:            
#         if math.sqrt(n).is_integer():
#             return True
#         else:
#             return False

# print(is_square(196))
# endregion
#region Exercise 5 02.06.2026

# Implement a function that adds two numbers
#  together and returns their sum in binary. The conversion
#  can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))

# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)


# def add_binary(a,b):
#     sum_num = a + b
#     binary_num = str(bin(sum_num))
#     corrected_version = binary_num[2:]
#     return corrected_version

# print(add_binary(1, 1))
#endregion
#region Exercise 6 02.06.2026
# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

# Examples:

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# However, the arrays can have varying lengths, not just limited to 4.

# def binary_array_to_number(arr):
#     string_Number = ''
#     for i in arr:
#         string_Number += str(i)
    
#     return int(string_Number, 2)

# print(binary_array_to_number([1, 0, 1, 1]))
# endregion
#region Exercise 7 03.06.2026
# Description:
# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# def reverse_words(text):
#     reversed = " ".join([word[::-1] for word in text.split(" ")])
#     return reversed

# print(reverse_words('hello my name is john'))
# print('john'[::-1])


# print( 'hello '.split(' '))
# endregion
#region Exercise 8 03.06.2026
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.
vogals = ['a', 'e', 'i', 'o', 'u']
def get_count(sentence):
    vogals_count = 0

    for i in sentence:
        if i in vogals:
            vogals_count += 1
    return vogals_count

print(get_count('hello mr johnathan wheatley how are you doing on this fine day?'))
# endregion
#region Exercise 9 03.06.2026
# Create a function called one that accepts two params:

# a sequence
# a function
# and returns true only if the function in the params returns true for exactly one (1) item in the sequence.

# Example
# one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten) -> true
# one([1, 3, 5, 6, 99, 88, 3], bigger_than_ten) -> false
# one([1, 3, 5, 6, 5, 1, 3], bigger_than_ten) -> false
def one(xs, f):
    count = 0 
    for i in xs:
        if f(i):
            count += 1
    
    if count == 1:
        return True
    else:
        return False
        


def bigger_than_ten(j):
    if j > 100:
        return True
    else:
        return False
print(one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten))
#endregion
#region Exercise 10 03.06.2026
# In this Kata your task will be to return
#  the count of pairs that have consecutive numbers. The first pair 
# consists of the first and second element of the input, the second pair is the next two 
# elements (3rd and 4th), etc. If the input ends with an element without a pair, it should be ignored.
# For example, [1,2,5,8,-4,-3,7,6,5] has 3 such pairs.
#  Candidate pairs are selected as follows: [(1,2), (5,8), (-4,-3), (7,6), 5].
# the first pair is (1,2) and the numbers in the pair are consecutive; Count = 1
# the second pair is (5,8) and the numbers are not consecutive.
# the third pair is (-4,-3), consecutive. Count = 2.
# the fourth pair is (7,6), also consecutive. Count = 3.
# the last element has no pair, so we ignore.

def pairs(arr):
    count = 0
    for i in range(0, len(arr) - 1, 2):
        a, b = arr[i], arr[i + 1]
        if abs(a - b) == 1:
            count += 1
    return count
print(pairs([(1,2), (5,8), (-4,-3), (7,6), 5]))
#endregion
