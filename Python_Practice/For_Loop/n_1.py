# WAP to display number in descending order

def descending(num):
    for i in range(num,0,-1):
        print(i)

num = int(input("Enter number : "))
# descending(num)

print([i for i in range(num,0,-1)])

