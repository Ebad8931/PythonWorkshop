"""
# Taking input
major = input("Enter your Major: ")
no_of_credits = int(input("Enter the number of credits you are enrolled in: "))
year, gpa = input("Enter your Year, GPA: ").split(',')
gpa = float(gpa)
print('You are enrolled in ' + year + ' year in ' + major +
      ' Major. You have currently taken', no_of_credits,
      'credits and your GPA is ' + str(gpa))
"""

# simple if statement
test = 67 < 78
if test:
    print('logical value of test is True')

# simple if-else statement
condition = 24 == 56
if condition:
    print('Condition is True')
else:
    print('Condition is False')

# if-elif statements
number = 12
if (number >= 0) and (number < 10):
    print('Number is in the range 0 to 9')
elif (number >= 10) and (number < 20):
    print('Number is in the range 10 to 19')
elif (number >= 20) and (number < 30):
    print('Number is in the range 20 to 29')
else:
    print('Number is negative or greater than 29')


# for loop
for i in range(5):
    print('hello world')

# while loop
count = 0
while count < 5:
    print('hello world')
    count += 1

# Break Statement
for i in range(5, 10):
    print(i)
    if i == 8:
        break

# Continue Statement
for i in range(5, 10):
    if i == 7 or i == 8:
        continue
    print(i)


