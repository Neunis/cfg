"""
Naomi Nunis
Code First Girls
Homework 1
10/26/23
"""

""" 
Question 1 
I am building some very high quality chairs and need exactly four nails for each chair. 
I've written a program to calculate how many nails I need to buy to build these chairs. 
chairs = '15' 
nails = 4 
total_nails = chairs * nails 
message = 'I need to buy {} nails'.format(total_nails) 
print('You need to buy {} nails'.format(message)) 
When I run the program it tells me that I need to buy 15151515 nails. 
This seems like a lot of nails. Is my program calculating the total number of nails correctly? 
What is the problem? How do I fix it? 
"""

#Solution - 1
# No, The program currently is duplicating the string value of chairs '15' four times instead of calculating the values
# This is due to the value of chairs being a string and the value of nails being an int
# One solution is below by manually converting and ensuring both values are int
chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)
#alternatively converting string value chair to int for similar outcome
chairs = '15'
nails = 4
total_nails = int(chairs) * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)
# I'd also update print in both versions to avoid duplicate messaging


"""
Question 2 
I('m trying to run this program, but I get an error. '
  'What is the error telling me is wrong? How do I fix the program?) 
my_name = Penelope 
my_age = 29 
message = 'My name is {} and I am {} years old'.format(my_name, my_age) 
print(message)
"""

#Solution - 2
# the NameError is not defined, meaning since Penenlope is of type string
# the string needs to be surrounded by quotes to reflect that
my_name = "Penelope"
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

"""
Question 3 
I have a lot of boxes of eggs in my fridge 
I want to calculate how many omelettes I can make.
Write a program to calculate this. 
Assume that a box of eggs contains six eggs 
I need four eggs for each omelette, 
but I should be able to easily change these values if I want. 
The output should say something like "You can make 9 omelettes with 6 boxes of eggs". 
"""

#Solution - 3
# Considering eggs amount, number of eggs, and eggs needed for omelette are subject to change
# The program allows for calculation of an omelette and the results to be printed out.
eggs_in_box = 6
box_of_eggs = 1
omelettes = 4
total_omelettes = (box_of_eggs*eggs_in_box)/omelettes
output = "You can make {} omelettes with {} box(es) of eggs". format(total_omelettes, box_of_eggs)
print(output)
