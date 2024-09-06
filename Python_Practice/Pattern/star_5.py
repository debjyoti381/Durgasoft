# WAP to print Right Angle Triangle with pattern with * symbol

# Method 1
def tri(n):
    for i in range(1,n+1):
        for j in range(i):
            print('*', end=' ')
        print()

# Method 2

def tri_1(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print()

n = int(input("Enter the no of row : "))
tri_1(n)


