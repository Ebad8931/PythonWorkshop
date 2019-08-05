# creating a string
text = 'N2E Python Programming'

# Accessing a letter in a String
print(text[0])
print(text[5])
print(text[-1])
print(text[-4])

# Accessing letters in a string
print(text[1:5])
print(text[:6])
print(text[8:])

# creating new text
new_text = 'Hello world!'

# Concatenation of stings
print(text + ' & ' + new_text)

# Updating Strings: Output Hello Python using text and new_text variables
print(new_text[:6] + text[4:10])
# Replacing Python with Java
# text[4:10] = 'Java' results in an error 'str' object does not support item assignment
print(text.replace('Python', 'Java'))

# Count the number of letters (spaces included) in the string
print(len(text))
# Change Case
print(text.upper())
print(text.lower())

# Checking Presence
print('Py' in text)
print('P' in text)
print('w' in text)
print('t' not in text)
print(not 'x' in text)      # warning
print(text.startswith('N2'))
print(text.endswith('g'))

# String formatting
print('You are enrolled in {year} year in {major} Major. You have '
      'currently taken {no_of_credits} credits and your '
      'GPA is {gpa}'.format(year='Sophomore',
                            major='Computer Engineering',
                            no_of_credits=15, gpa=3.58))

