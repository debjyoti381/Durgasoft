# WAP tyo print to write a square patternwith fixed digit in every line 
# Method -1
def square_num(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i, end=' ')
        print()


# Method -2
def square_num_1(n):
    for i in range(1,n+1):
        print((str(i)+' ')*n)

        
n = int(input("Enter a number : "))
square_num_1(n)