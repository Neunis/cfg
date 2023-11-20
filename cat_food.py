#example for formatting strings
user_name = 'sarah_1987'
age = 23
output = '{} is {} years old'.format(user_name, age)
print(output)

#cat exercise to practice formating with + concat
cats = 10
cans = 2
total_cans = cats * cans
output = str(cats) + " cats eat " + str(total_cans) + " cans"
print(output)

cats = 10
cans = 2
days = 7
total_cans = cats * cans * days
msg = str(cats) + " cats eat " + str(total_cans) + " cans in " + str(days) + " days"
print(msg)

#final results formatting with format tool
cats = 10
cans = 2
total_cans = cats * cans
output = "{} cats eat {} cans".format(cats, total_cans)
print(output)