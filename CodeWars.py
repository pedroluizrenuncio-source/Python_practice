import math

#region Exercise 1. 
#
# def square_digits(num):
#     new_number = ''
#     for element in str(num):
#         new_number += str(int(element)**2)
#     return new_number

# print(square_digits(220384))
# endregion
#region Exercise 2 01.06.2026

# def circle_area(r):
#     if r <= 0:
#         raise ValueError("Radius must be positive")
    
#     area = math.pi * r ** 2
#     return round(area, 2)

# print(circle_area(43.2673))  # 5881.25
# endregion
#region Exercise 3 01.06.2026 
# !def validate_pin(pin):
#     if len(pin) in [4, 6] and pin.isdigit():
#         return True
#     else:
#         return False
    
# print(validate_pin("123456"))
# endregion
#region Exercise 4(02/06/2026)
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
# def add_binary(a,b):
#     sum_num = a + b
#     binary_num = str(bin(sum_num))
#     corrected_version = binary_num[2:]
#     return corrected_version

# print(add_binary(1, 1))
#endregion
#region Exercise 6 02.06.2026
# def binary_array_to_number(arr):
#     string_Number = ''
#     for i in arr:
#         string_Number += str(i)
    
#     return int(string_Number, 2)

# print(binary_array_to_number([1, 0, 1, 1]))
# endregion
#region Exercise 7 03.06.2026
# def reverse_words(text):
#     reversed = " ".join([word[::-1] for word in text.split(" ")])
#     return reversed

# print(reverse_words('hello my name is john'))
# print('john'[::-1])


# print( 'hello '.split(' '))
# endregion
#region Exercise 8 03.06.2026
# vogals = ['a', 'e', 'i', 'o', 'u']
# def get_count(sentence):
#     vogals_count = 0

#     for i in sentence:
#         if i in vogals:
#             vogals_count += 1
#     return vogals_count

# print(get_count('hello mr johnathan wheatley how are you doing on this fine day?'))
# endregion
#region Exercise 9 03.06.2026
# def one(xs, f):
#     count = 0 
#     for i in xs:
#         if f(i):
#             count += 1
    
#     if count == 1:
#         return True
#     else:
#         return False
        


# def bigger_than_ten(j):
#     if j > 100:
#         return True
#     else:
#         return False
# print(one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten))
#endregion
#region Exercise 10 03.06.2026
# def pairs(arr):
#     count = 0
#     for i in range(0, len(arr) - 1, 2):
#         a, b = arr[i], arr[i + 1]
#         if abs(a - b) == 1:
#             count += 1
#     return count
# print(pairs([(1,2), (5,8), (-4,-3), (7,6), 5]))
#endregion
#region Exercise 11 04.06.2026
# def disemvowel(string_):
#     vowels = set('aeiouAEIOU')
#     return ''.join(c for c in string_ if c not in vowels)

# print(disemvowel('hello my name is pEdro'))
#endregion
#region Exercise 12 04.06.2026 
# def high_and_low(numbers):
#     nums = [int(n) for n in numbers.split()]
#     return f"{max(nums)} {min(nums)}"


# print(high_and_low(("1 2 3 4 5")))
#endregion
#region Exercise 13 04.06.2026
# def descending_order(num):
#     numbers = [int(n) for n in str(num)]
#     return int(''.join(str(n) for n in sorted(numbers, reverse=True)))
# endregion
#region Exercise 14 05.06.2026
# def filter_list(l):
#     filtered_list = [x for x in l if isinstance(x, int)]
#     return filtered_list
# print(filter_list([1,2,'aasf','1','123',123]))
#endregion
#region Exercise 15 05.06.2026

# def get_middle(s):
#     if len(s) %2 != 0:
#         return s[int((len(s)/ 2))]
#     elif len(s) %2 == 0:
#         return f'{s[int(len(s)/2-1)] + s[int(len(s)/2 )]}'

# print(get_middle('A'))
#endregion
#region Exercise 16 05.06.2026
# def find_short(s):
#     return min(len(word) for word in s.split())

# print(find_short('hello johnny how are you '))
# endregion
#region Exercise 17 06.06.2026
# def DNA_strand(dna):
#     complement = ''
#     for n in dna:
#         if n == 'A':
#             complement += 'T'
#         elif n == 'T':
#             complement += 'A'
#         elif n == 'C':
#             complement += 'G'
#         elif n == 'G':
#             complement+= 'C'
#     return complement

# print(DNA_strand('ATTGC'))
#endregion
#region Exercise 18 06.06.2026
# def maskify(cc):
#     return '#' * (len(cc) - 4) + cc[-4:]

# print(maskify("4556364607935616"))
#endregion
#region Exercise 19 07.06.2026
# reate a function that returns the sum of the two lowest positive numbers
#  given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455

def sum_two_smallest_numbers(numbers):
    n1, n2 = sorted(numbers)[:2]
    return n1 + n2

print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453] ))
#endregion

#region Exercise 20 07.06.2026
# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Input = ["Ryan", "Kieran", "Jason", "Yous"]
# Output = ["Ryan", "Yous"]

# Input = ["Peter", "Stephen", "Joe"]
# Output = []

def friend(x):
    friend = []
    for i in x:
        if len(i) == 4:
            friend.append(i)
    return friend
print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
            
    #Code
#endregion 
#region Exercise 21 07.06.2026
def odd_or_even(arr):
    total = 0
    for i in arr:
        total += i
    if total % 2 == 0:
        return 'even'
    else:
        return 'odd'

print(odd_or_even([0, 1, 4]))
#endregion 
#region Exercise 22 07.06.2026
# Given an array of integers, remove the smallest value. 
# Do not mutate the original array/list. If there are multiple elements with the same value, 
# remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

# Examples
# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]

def remove_smallest(numbers):
    if not numbers:
        return []
    minnimal = list(numbers)
    minnimal.remove(min(minnimal))
    return minnimal

print(remove_smallest([2,2,1,2,1]))