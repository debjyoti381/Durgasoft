# Find the Biggest Number among 3 num
def biggest(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(f"{n1} is Biggest")
    elif n2>n3:
        print(f"{n2} is Biggest")
    else:
        print(f"{n3} is Biggest")

n = input("Enter 3 number separated by ',' : ")
n1,n2,n3 = map(int,n.split(','))
biggest(n1,n2,n3)