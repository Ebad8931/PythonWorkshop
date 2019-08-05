from random import randint

# Previous Examples of functions
print('Hello world')
range(5, 17, 2)
len('python')


# defining a function
def hello():
    print('hello world')


# calling the function
hello()


def add(num1, num2):    # num1 and num 2 are arguments
    return num1 + num2  # result is returned


# Function Calling
total = add(7, 9)
print(total)


def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add_numbers(5, 6, 8, 4, 2))
print(add_numbers(234, 543))
print(add_numbers(34, 56, 78, 5, 5.67, 2.45, 5*4))


def cool_function(a, b=4, c=10):
    # b and c are default value arguments
    print('a is', a, 'b is', b, 'c is', c)


cool_function(38, 49)      # a&b are passed c takes its default value
cool_function(54, c=74)    # c is keyword argument, b is default argument
cool_function(c=72, a=23)  # a&c are keyword arguments, b is default argument

data = [45, 35, 67]  # a = data[0], b = data[1], c = data[2]
cool_function(*data)       # * unpacks the list and passes it to the function

# random.randint(a,b) generates a random number N such that a <= N <= b
print(randint(1, 10))
print(randint(1, 10))
