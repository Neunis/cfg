"""
Naomi Nunis
Code First Girls
Homework 2
11/4/23
"""

"""
Question 1 
Explain what this program does 
for number in range(100): 
output = 'o' * number 
print(output) 

Explanation:
This for loop is iterating over a range of numbers from 0 to 99.
For each number in the range, the output variable stores how many 'o's will be listed. 
For example, 0 * 'o' = nothing is displayed, while 1 * 'o' = 'o' is displayed.
This behavior will continue until the 100th number, 99, resulting in a hill of 'o's, 
Ex:
0
00
000
0000
etc.
Once complete the loop behavior ends
"""

"""
Question 2
Your boss really likes calculating VAT on their purchases.
It is their favourite hobby.
They('ve written this code to calculate VAT and need your help to fix it.)

When your boss runs the program they get the following output:
None
Your boss expects the program to output the value 120. What is wrong? How do you fix it?

Problem: there is no way for the value calculated in the function calculate_vat(amount) to
be stored or returned/received. Currently even the print call is outside the function, so even
locally there is no formal way for the function to display results from function or store any meaningful value locally.  

def calculate_vat(amount):
amount * 1.2

total = calculate_vat(100)
print(total)

"""

#Solution:
# create a variable to store calculation locally in function
# return stored value in function
# call function with number of choice to be calculated
# print output
def calculate_vat(amount):
    total = amount * 1.2
    return total

print(calculate_vat(100))
