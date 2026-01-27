# PAT TASK:4
# 1. Two lists one with Even and other with Odd:

# Numbers_list = [10,501,22,37,100,999,87,351]
#
# # Separate even numbers
# Even_numbers = [num for num in Numbers_list if num % 2 == 0]
#
# # Separate odd numbers
# Odd_numbers = [num for num in Numbers_list if num % 2 != 0]
#
# print("Even numbers:", Even_numbers)
# print("Odd numbers:", Odd_numbers)

# 2. Count and list of prime numbers:

# Numbers_list = [10,501,22,37,100,999,87,351]
#
# prime_numbers =[]
#
# for num in Numbers_list:
#     if num > 1:
#         isPrime = True
#         for i in range (2,num):
#             if num % i == 0:
#                 isPrime = False
#                 break
#         if isPrime:
#                 prime_numbers.append(num)
# print("Prime Numbers: ", prime_numbers)
# print("Count of Prime Numbers: ", len(prime_numbers))

# 3.To find happy number from list: Happy number is number that eventually reaches 1 when the sum of squares of its digits

# def is_happy(n):
#     Value = set()
#     while n != 1 and n not in Value:
#         Value.add(n)
#         n =sum(int(digit)**2 for digit in str(n))
#     return n == 1
# Happy_list = [10,501,22,37,100,999,87,351]
# Happy_numbers = []
#
# for num in Happy_list:
#     if is_happy(num):
#         Happy_numbers.append(num)
#
# print("The list of happy numbers is:" , Happy_numbers)

# 4. To find sum of first and last digit of an integer:
# Convert integer into string
# num = int(input("Enter your number: "))
# num_str = str(num)
# first_digit = int (num_str[0])
# last_digit = int (num_str[-1])
#
# Sum_digits = first_digit + last_digit
#
# print ("Sum of first and last digits is", Sum_digits)

# 5. To find all ways to make RS.10, using RS.1, Rs.2, rs.5, rs.10

# # python
# def ways_to_make(amount=10):
#     solutions = []
#     for n1 in range(amount + 1):              # RS.1 coins
#         for n2 in range(amount // 2 + 1):     # RS.2 coins
#             for n5 in range(amount // 5 + 1): # RS.5 coins
#                 for n10 in range(amount // 10 + 1): # RS.10 coins
#                     total = n1*1 + n2*2 + n5*5 + n10*10
#                     if total == amount:
#                         solutions.append((n1, n2, n5, n10))
#     return solutions
#
# def print_solutions(solutions):
#     for i, (n1, n2, n5, n10) in enumerate(solutions, 1):
#         print(f"{i:2d}. {n1} x RS.1  + {n2} x RS.2  + {n5} x RS.5  + {n10} x RS.10")
#     print(f"\nTotal ways: {len(solutions)}")
#
# if __name__ == "__main__":
#     sols = ways_to_make(10)
#     print_solutions(sols)

# 6. To find duplicate in three list:

# list1 = [1, 2, 3, 4, 5,7]
# list2 = [3, 4, 5, 6, 7, 8]
# list3 = [5, 6, 7, 8, 9, 10]
#
# duplicates = list (set(list1) & set(list2) & set(list3))
# print("Duplicate elements in all three lists:", duplicates)

# 7. Find the first non-repeating element in a list of integers:

# Numbers = [4, 5, 1, 2, 1, 0, 6, 4]
#
# for number in Numbers:
#     if Numbers.count(number) == 1:
#         print("The first non-repeating element is:", number)
#         break

# 8. Find the minimum element in  rated and sorted list:

# Numbers_list = [34, 15, 88, 2, 19, 7]
#
# Numbers_list.sort()
# print("Minium element in the list is:", Numbers_list[0])

# 9. Pyhon list and its value 59, Find triplet in list whose sum is equal to value 59

# Python_list =[10, 20, 30, 9]
# target = 59
#
# n = len(Python_list)
#
# for i in range(n):
#     seen = set ()
#     current_sum = target - Python_list[i]
#     for j in range(i + 1, n):
#         complement = current_sum - Python_list [j]
#         if complement in seen:
#             print("Triplet found:", (Python_list[i], Python_list[j], complement))
#         seen.add(Python_list[j])

# 10. List , Program to find its sub-list with sum equal to Zero:

# Python_list =[4, 2, -3, 1, 6]
#
# found = False
#
# for i in range(len(Python_list)):
#     current_sum = 0
#     for j in range(i, len(Python_list)):
#         current_sum += Python_list[j]
#         if current_sum == 0:
#             found = True
#             break
#     if found:
#         break
# if found:
#             print ("Sub-list with sum zero: ", Python_list[i:j+1])