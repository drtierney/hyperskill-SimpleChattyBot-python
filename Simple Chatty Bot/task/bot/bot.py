bot_name = "Monty"
birth_year = 2021

print("Hello! My name is {0}.".format(bot_name))
print("I was created in {0}.".format(birth_year))
print("Please, remind me your name.")

your_name = input()
print("What a great name you have, {0}!".format(your_name))
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is {0}; that's a good time to start programming!".format(age))
