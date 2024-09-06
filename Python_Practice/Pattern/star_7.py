# WAP to print Pyramid pattern with * symbol
# Method 1
def pyramid(n):
    for i in range(n):
        print((' '*(n-i-1)+("* ")*(i+1)))

# Method 2
def pyramid_1(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end= '')
        for k in range(i+1):
            print(" *", end='')
        print()


num = int(input("Please enter the number of row : "))
pyramid_1(num)