"""
Naomi Nunis
Code First Girls
Homework
11/16/23
"""


"""
Question 1 
I have a list of things I need to buy from my supermarket of choice. 

shopping_list = [ 
"oranges", 
"cat food", 
"sponge cake", 
"long-grain rice", 
"cheese board", 
] 
print(shopping_list[1]) 

I want to know what the first thing I need to buy is.
However, when I run the program it shows me a different answer to what I was expecting? 
What is the mistake? How do I fix it?

Answer: The mistake was using the number 1 instead of zero, by default in the CS world
everything starts at 0: lists, indexing, etc. 

In order to fix it change the print out statement as shown below.

"""

shopping_list = [
"oranges",
"cat food",
"sponge cake",
"long-grain rice",
"cheese board",
]

print(shopping_list[0])

"""
Question 2 
I'm setting up my own market stall to sell chocolates.
I need a basic till to check the prices of different chocolates that I sell. 
I've started the program and included the chocolates and their prices. 
Finish the program by asking the user to input an item and then output its price. 
"""

"""
chocolates = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,
}

user_choice = input("Choose which type of chocolate you'd like:\n white, milk, dark, or vegan:")

if user_choice in chocolates:
    print("{} chocolate costs ${}".format(user_choice, chocolates[user_choice]) )
else:
    print("Unfortunately, we are either out of stock or that is not an option.\n Thank you!")
"""

"""
Question 3 
Write a program that simulates a lottery. 
The program should have a list of seven numbers that represent a lottery ticket.
It should then generate seven random numbers. After comparing the two sets of numbers,
the program should output a prize based on the number of matches: 
● £20 for three matching numbers 
● £40 for four matching numbers 
● £100 for five matching numbers 
● £10000 for six matching numbers 
● £1000000 for seven matching numbers 

"""

import random

"""
def lotteryTicket():
    num_list = []
    count = 0
    while count < 7:
        number_generator = random.randint(1,25)
        num_list.append(number_generator)
        count += 1
    return num_list
"""

lottery_list = list(random.randint(1,25) for i in range(7))
random_list = list(random.randint(1,25) for i in range(7))

print("The lottery numbers are {}\nThe random numbers chosen are{}".format(lottery_list, random_list))

if lottery_list == random_list:
    print("Congrats you win ● £1000000 for seven matching numbers")

count = 0
for x in lottery_list:
    for y in random_list:
        if x == y:
            count +=1

if count == 3:
    print("£20 for three matching numbers")
elif count == 4:
    print("£40 for four matching numbers")
elif count == 5:
    print("£100 for five matching numbers")
elif count == 6:
    print("£10000 for six matching numbers")
else:
    print("There are no matching numbers")







