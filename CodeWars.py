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
#region Exercise 4 02.06.2026
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
# def sum_two_smallest_numbers(numbers):
#     n1, n2 = sorted(numbers)[:2]
#     return n1 + n2

# print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453] ))
#endregion
#region Exercise 20 07.06.2026
# def friend(x):
#     friend = []
#     for i in x:
#         if len(i) == 4:
#             friend.append(i)
#     return friend
# print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
        
#endregion 
#region Exercise 21 07.06.2026
# def odd_or_even(arr):
#     total = 0
#     for i in arr:
#         total += i
#     if total % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'

# print(odd_or_even([0, 1, 4]))
#endregion 
#region Exercise 22 07.06.2026
# def remove_smallest(numbers):
#     if not numbers:
#         return []
#     minnimal = list(numbers)
#     minnimal.remove(min(minnimal))
#     return minnimal

# print(remove_smallest([2,2,1,2,1]))
#endregion
#region Exercise 23 13.06.2026
# def find_next_square(sq):
#     nextsq = False
#     print(math.sqrt(sq))    # Return the next square if sq is a square, -1 otherwise
#     if math.sqrt(sq) % 1 == 0 :
#         new_numb = sq
#         while not nextsq:
#             new_numb += 1
#             if math.sqrt(new_numb) %1 ==0:
#                 nextsq = True
#                 return new_numb
#             else: continue
#     else:
#         return -1
    
# print(find_next_square(625))
#endregion
#region Exercise 24 13.06.2026
# def capitals(word):
#     capitals_list = []
#     for i, char in enumerate(word):
#         if char == char.upper():
#             capitals_list.append(i)
#     return capitals_list
# print(capitals("CodEWaRs"))
#endregion
#region Exercise 25 13.06.2026
# def sum_digits(number):
#     summed = 0
#     absolute = abs(number)
#     stringed = str(absolute)
#     for i in stringed:
#         summed += int(i)
#     return summed
# print(sum_digits(99))
#endregion
#region Exercise 26 13.06.2026
# def accum(st):
#     accumulated = []
#     for i, char in enumerate(st):
#         accumulated.append(char.upper() + (char *(i)).lower())
#     # return '-'.join[]
#     return '-'.join(accumulated)

# print(accum("RqaEzty"))
#endregion
#region Exercise 27 13.06.2026
# def to_jaden_case(string):
#    return ' '.join(i.capitalize() for i in string.split())
# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
#endregion
#region Exercise 28 13.06.2026
# def solution(text, ending):
    
#     if len(ending)> len(text):
#         return False
#     elif text[-(len(ending)):] == ending:
#         return True
#     else:
#         return False 
# print(solution( "this",    "fails"))
#endregion
#region Exercise 29 14.06.2026
# def knight_vs_rook(knight, rook):
#     #position horse and rook 
#     p_horse_row = knight[0] 
#     p_horse_column =(ord(knight[1])-64)
#     p_rook_row = rook[0] 
#     p_rook_column =(ord(rook[1])-64)
#     summed = (abs(p_horse_row - p_rook_row), abs(p_horse_column - p_rook_column))
#     #configuring the rook 
#     if rook[1] == knight[1] or rook[0] == knight[0]:
#         return 'Rook'
#     elif summed == (2,1) or summed == (1,2):
#         return 'Knight'           
#     else:
#         return None
# print(knight_vs_rook((7, 'B'), (2, 'F')))
#endregion 
#region Exercise 30 14.06.2026
# def caffeine_buzz(n):
#     mocha_word = ''
#     if n %3 == 0 and n %4 != 0:
#         mocha_word += 'Java'
#         if n%3 == 0 and n %2 == 0:
#                 mocha_word+='Script'
    
#     elif n %3 == 0 and n %4 == 0:
#         mocha_word += 'Coffee'
#         if n%3 == 0 and n %2 == 0:
#             mocha_word+='Script'
#     else: mocha_word += 'mocha_missing!'
#     return mocha_word
    
# print(caffeine_buzz(12))
#endregion
#region Exercise 31 14.06.2026
# def stalin_sort(arr):
#     if not arr:
#         return []
#     survivors = [arr[0]]
#     for val in arr[1:]:
#         if val >= survivors[-1]:
#             survivors.append(val)
#         else:
#             print("Расстрелять!")
#     return survivors

# print(stalin_sort([3, 1, 4, 1, 5, 9, 2]))     
# endregion   
#region Exercise 32 14.06.2026
# def solution(number):
#     if number < 0:
#       return 0

#     numbers = []
#     for i in range(0, number):
#       if i %3 == 0 or i %5 ==0:
#          numbers.append(i)
    
#     return sum(numbers)
# print(solution(6))
#endregion
#region Exercise 33 14.06.2026
# def divisors(integer):
#     result = []
#     for i in range(2, integer):
#         if integer % i == 0:
#             result.append(i)
#     if not result:
#         return f"{integer} is prime"
#     return result
# print(divisors(24))
#endregion
#region Exercise 34 17.06.2026  
def complete(s):
    for k in range(1, len(s) + 1):
        if s[k:] == s[k:][::-1]:
            return s + s[:k][::-1]


# print(complete('aab'))
#endregion
#region Exercise 35 17.06.2026 

def split_odd_and_even(n):
    stringed = str(n)
    result = []
    current_group = stringed[0]
    current_parity = int(stringed[0]) % 2

    for i in stringed[1:]:
        if int(i) % 2 == current_parity:
            current_group += i
        else:
            result.append(int(current_group))
            current_group = i
            current_parity = int(i) % 2

    result.append(int(current_group))
    return result
#endregion
#region Exercise 36 17.06.2026
def eq_all(iterable):
    items = list(iterable)
    if not items:
        return True
    for i in range(len(items) - 1):
        if items[i] != items[i+1]:
            return False
    return True
#endregion