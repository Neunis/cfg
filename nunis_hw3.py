"""
Naomi Nunis
Code First Girls
Homework 3
11/14/23
"""

"""
Question 1 
Create a program that tells you whether or not you need an umbrella when you leave the house. 
The program should: 
1. Ask you if it is raining using input() 
2. If the input is 'y', it should output 'Take an umbrella' 
3. If the input is 'n', it should output 'You don't need an umbrella' 
"""


weather_status = input("Is it raining outside? y/n ")
weather_status = weather_status.lower()

if weather_status == 'y':
    print("You should take an umbrella.")
elif weather_status == 'n':
    print("You don't need an umbrella.")
else:
    print("That is not a proper response, therefore I cannot help you at this time.")



"""
Question 2 
I'm on holiday and want to hire a boat. 
The boat hire costs £20 + a refundable £5 deposit. 
I've written a program to check that I can afford the cost, but something doesn't seem right. 
Have a look at my program and work out what I've done wrong 

my_money = input('How much money do you have? ') 
boat cost = 20 + 5
if my_money < boat_cost: 
print('You can afford the boat hire') 
else: 
print('You cannot afford the board hire') 

Errors found and corrected below:
- boat cost in line 1 needs to match boat_cost in line 2
- my money input needs to be converted into a integer
- indent the print statements
- the first print statement needs to be switched with the second print statement
particularly the words can and cannot
- future note: add a error response if someone does not input a number, for example 'hi'
"""


my_money = int(input('How much money do you have? '))
boat_cost = 20 + 5
if my_money < boat_cost:
    print('You cannot afford the boat hire')
else:
    print('You can afford the board hire')



"""
Question 3 
Your friend works for an antique book shop that sells books 
between 1800 and 1950 and wants to quickly categorise books 
by the century and decade that they were written. 
Write a program that takes a year (e.g. 1872) and 
outputs the century and decade (e.g. "Nineteenth Century, Seventies") 

"""

def CenturyDecade(year):
    y = str(year)
    notes = []
    for l in y:
        notes.append(l)

    century_dic = {
        1: "Eighteenth Century",
        2: "Nineteenth Century"
    }

    decades_dic = {
        1: "Tens",
        2: "Twenties",
        3: "Thirties",
        4: "Forties",
        5: "Fifties",
        6: "Sixties",
        7: "Seventies",
        8: "Eighties",
        9: "Nineties"
    }

    century_num = notes[1]
    decade_num = notes[2]

    if century_num == "8":
        century_name = century_dic[1]
    elif century_num == "9":
        century_name = century_dic[2]
    else:
        century_name = "century out of range"

    if decade_num == "1":
        decade_name = decades_dic[1]
    elif decade_num == "2":
        decade_name = decades_dic[2]
    elif decade_num == "3":
        decade_name = decades_dic[3]
    elif decade_num == "4":
        decade_name = decades_dic[4]
    elif decade_num == "5":
        decade_name = decades_dic[5]
    elif decade_num == "6":
        decade_name = decades_dic[6]
    elif decade_num == "7":
        decade_name = decades_dic[7]
    elif decade_num == "8":
        decade_name = decades_dic[8]
    elif decade_num == "9":
        decade_name = decades_dic[9]
    else:
        decade_name = "decade out of range"

    result = ("{}, {}".format(century_name, decade_name))
    return result




book_year = int(input("What is the year that this book was written? "))

if book_year in range(1800,1951):
    print(CenturyDecade(book_year))
else:
    print("This book does not meet the 1800-1950 criteria")

