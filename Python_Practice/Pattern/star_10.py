# WAP to print Dimond Pyramid with * symbol. 
def diamond(n):
    for i in range(n):
        print((' '*(n-i-1)+("* ")*(i+1)))
    for i in range(n-1):
        print(' '*(i+1)+ '* '*(n-i-1))

num = int(input("Enter num of row : "))
diamond(num)