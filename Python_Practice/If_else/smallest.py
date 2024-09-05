# Find the smallest number among 3 number
def smallest(n1,n2,n3):
    if n1<n2 and n1<n3:
        print(f"{n1} is Smallest")
    elif n2<n3:
        print(f"{n2} is Smallest")
    else:
        print(f"{n3} is Smallest")

n = input("Enter 3 number seperated by ',' : ")
n1,n2,n3 = map(int,n.split(","))
smallest(n1,n2,n3)