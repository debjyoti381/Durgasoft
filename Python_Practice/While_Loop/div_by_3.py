# WAP to print numbers from 1 to n divisible by 3:
def div_by_3(num):
    n = 1
    while n<=num:
        if n % 3 == 0:
            print(n)
        n+=1
num = int(input("Enter the number : "))
div_by_3(num)