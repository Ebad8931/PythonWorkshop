# Problem Link https://www.hackerrank.com/challenges/staircase/problem

lines = int(input('Enter the number of lines to be displayed: '))
for i in range(lines):
    print((lines-1-i)*' ' + '#'*(i+1))
