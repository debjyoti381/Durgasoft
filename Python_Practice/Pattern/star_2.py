# WAP to print square pattern with * symbols
# Medthod - 1
def square(n):
    for i in range(n):
        for j in range(n):
            print('*', end= ' ')
        print()

# Method -2 
def square_1(n):
    for i in range(n):
        print('* '*n)

num = int(input("Enter a number : "))
square_1(num)