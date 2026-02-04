# # 1. Using lambda functions to filter people under 18 and map remaining in new list
#
# people = [
#     {"name": "Alice", "age": 17},
#     {"name": "Bob", "age": 20},
#     {"name": "Charlie", "age": 16},
#     {"name": "David", "age": 22},
#     {"name": "Eve", "age": 15},
#     {"name": "Frank", "age": 19}
# ]
# adults = list(map(lambda person: person["name"],
#                   filter(lambda person: person["age"] >= 18, people)))
# print(adults)
#
# #2. From the list of numbers, use reduce function and a lambda expression to calculate the product of all the numbers.
#
# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)
#
# # 3.list of comprehension that creates a list of squares of even numbers from given list,
# # using lambda function to check even numbers
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result =[(lambda x: x * x)(num) for num in numbers if num % 2 == 0]
# print(result)
#
# # 4. lambda function to check if a string is number:
#
# is_number = lambda s: s.isdigit()
# test_strings = ["123", "abc", "456def", "789"]
# results = {s: is_number(s) for s in test_strings} #s is each string in test_strings, checking if it is number or not
# print(results)
#
# #5. use a lambda function to extract the year, month, and day from a datetime object.
#
# from datetime import datetime                           #importing datetime module
# dt = datetime(2026, 2, 4, 14, 30, 0)             # February 4, 2026, 14:30:00
# extract_date = lambda dt: (dt.year, dt.month, dt.day)             #function to extract year, month, day
# year, month, day = extract_date(dt)                                #unpacking the tuple returned by lambda function
# print(f"Year: {year}, Month: {month}, Day: {day}")                 #printing the extracted values
#
# #6.using lambda function to generate fibonacci sequence up to n terms.
# from functools import reduce
#
# fib = lambda n: [] if n <= 0 else [0] if n == 1 else reduce(      #number of terms n, return empty list if n<=0, return [0] if n==1
#     lambda acc, _: acc + [acc[-1] + acc[-2]],                     #accumulator acc and _ (dummy variable)
#     range(n - 2),                                                 #range of n-2 because first two terms are already defined                                               #initial accumulator value
#     [0, 1]                                                        #starting list with first two fibonacci numbers
# )
# print(fib(10))