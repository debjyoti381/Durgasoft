# WAP to print sum of first n numbers
def sum(num):
    n = 1
    sum = 0
    while n<=num:
        sum+=n
        n+=1
    print(sum)

num = int(input("Enter num : "))
sum(num)