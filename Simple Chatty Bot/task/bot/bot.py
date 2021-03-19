bot_name = "Monty"
birth_year = 2021

print("Hello! My name is {0}.".format(bot_name))
print("I was created in {0}.".format(birth_year))
print("Please, remind me your name.")

your_name = input()
print("What a great name you have, {0}!".format(your_name))
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
print("Your age is " + str(age) + "; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
num = int(input())
counter = 0

while counter <= num:
    print("{0} !".format(counter))
    counter += 1
print("Completed, have a nice day!")
