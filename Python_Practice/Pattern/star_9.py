# WAP to print Right Half Dimond Pyramid with * symbol. 
def diamond(n):
    for i in range(n):
        print('* '*(i+1))
    for i in range(n-1):
        print("* "*(n-i-1))

num = int(input("Enter num of row : "))
diamond(num)