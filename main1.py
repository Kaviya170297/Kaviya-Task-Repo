# PAT-TASK 3:
#
# 1. Guess the number:

import random
#
# Numbers_Challenge = random.randint(1, 10)
# attempts =4
#
# while attempts > 0:
#     Guess = int(input("Guess a number between 1 and 10: "))
#     if Guess == Numbers_Challenge:
#         print ("You guessed correctly!")
#         break
#     else:
#         attempts -= 1
#         print ("Wrong. Try again!, attempts left: ", + attempts)
#
#     if attempts == 0:
#         print ("Game Over! Correct number:", Numbers_Challenge)

# 2. Word Scramble:
#
# words = ["python","javascript","java","automation","pytest","guvi","selenium"]
#
# #select random word
# word=random.choice(words)

# To scramble a word from word list:
# scrambled = "".join(random.sample(word, len(word))).lower()
# print ("Scrambled word: ", scrambled)
# attempts = 3
# # To guess from multiple attempts:
# while attempts > 0:
#     Guess = input("Scrambled word: ")
#     if Guess == word:
#         print("Correct ,You find it right")
#         break
#     else:
#         attempts -= 1
#         print("Wrong answer!, attempts left: ",+attempts)
# if attempts == 0:
#     print("Game over! The Correct word is:", word)
