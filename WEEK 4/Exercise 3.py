
import random

secret = random.randint(1, 10)
user_answer = 0

while secret != user_answer:
    user_answer = int(input("Guess the number from 1 to 10: "))
