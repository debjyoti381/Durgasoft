# WAP to display odd number from 0-20:
# Type 1
def odd(num):
    for i in range(0,num+1):
        if i%2!=0:
            print(i)


# Type 2
def odd_1(num):
    for i in range(1,num+1,2):
        print(i)


# Type 3
num = int(input("Enter a number : "))

print([x for x in range(1,num+1,2)])
