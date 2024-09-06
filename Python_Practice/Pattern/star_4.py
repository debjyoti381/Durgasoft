# WAP to print square pattern with alphabet symbols

# Method 1
def square_alpha(n):
    for i in range(n):
        for j in range(n):
            print(chr(65+i), end=" ")
        print()

# Method 2
def square_alpha_1(n):
    for i in range(n):
        print((chr(65+i)+' ')*n)


n = int(input("Enter the number of row : "))
square_alpha_1(n)