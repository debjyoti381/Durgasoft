# WAP to print Invented Right angle triangle pattern with * symbol
# Method 1
def triangle(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*", end=' ')
        print()


# Method 2
def triangle_1(n):
    for i in range(n):
        print('* ' * (n-i))

n = int(input("Enter the number of row : "))
triangle_1(n)

