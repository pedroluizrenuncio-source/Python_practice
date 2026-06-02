import math

# 1. For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# def square_digits(num):
#     new_number = ''
#     for element in str(num):
#         new_number += str(int(element)**2)
#     return new_number

# print(square_digits(220384))


#/*2. # Complete the function which will return the area of a circle with the given radius.

# Returned value is expected to be accurate up to tolerance of 0.01.

# If the radius is not positive, raise ValueError.

# Example:

# circle_area(43.2673)      # returns 5881.248  (± 0.01)
# circle_area(68)           # returns 14526.724 (± 0.01)
# circle_area(0)            # raises ValueError
# circle_area(-1)           # raises ValueError

def circle_area(r):
    if r <= 0:
        raise ValueError("Radius must be positive")
    
    area = math.pi * r ** 2
    return round(area, 2)

print(circle_area(43.2673))  # 5881.25


#3. ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    if len(pin) in [4, 6] and pin.isdigit():
        return True
    else:
        return False
    
print(validate_pin("123456"))

# 4. Take 2 strings s1 and s2 including only letters from a to z. 
# Return a new sorted string (alphabetical ascending),
#  the longest possible, containing distinct letters
#  - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    new_a = a1 
    