# Wtite a program to print '*' in a same line 
def star(n):
    for i in range(n):
        print('*', end=' ')
num =int(input("Enter a number : "))
star(num)