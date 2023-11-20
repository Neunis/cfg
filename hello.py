print('Hello, World!')

print('I hope it is sunny this weekend')

print("Cat" + str(3))

print('spaghetti')
food = 'spaghetti'
print(food)

oranges = 12

cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
print(str(oranges) + " oranges")
print("costs " + str(total_cost))


# A program to calculate the cost of some oranges w/ formatting tool
oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
output = "{} oranges costs £{}".format(oranges, total_cost)
print(output)

# A program to calculate the cost of some oranges with + concat
oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
output = str(oranges) + " oranges costs £" + str(total_cost)
print(output)


days = 31
hours = "24"
total_hours = days * hours
msg = "There are {} in {} days".format(total_hours, days)
print(msg)


         
