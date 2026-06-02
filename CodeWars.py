import math

# 1. For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# def square_digits(num):
#     new_number = ''
#     for element in str(num):
#         new_number += str(int(element)**2)
#     return new_number

# print(square_digits(220384))

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
  

def is_square(n):    
    if n < 0:
        return False
    else:            
        if math.sqrt(n).is_integer():
            return True
        else:
            return False

print(is_square(196))
# endregion
#region Exercise 5 02.06.2026

# Implement a function that adds two numbers
#  together and returns their sum in binary. The conversion
#  can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))

# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)


def add_binary(a,b):
    sum_num = a + b
    binary_num = str(bin(sum_num))
    corrected_version = binary_num[2:]
    return corrected_version

print(add_binary(1, 1))
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

def binary_array_to_number(arr):
    string_Number = ''
    for i in arr:
        string_Number += str(i)
    
    return int(string_Number, 2)

print(binary_array_to_number([1, 0, 1, 1]))
