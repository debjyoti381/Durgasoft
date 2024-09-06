# WAP to generate prime numbers which are less than or equal the given number ?
def prime(n):
    n1 = 2
    while n1<=n:
        is_prime = True
        for i in range(2,n1//2+1):
            if n1 % i == 0:
                is_prime = False
                break
        if is_prime == True:
            print(n1, end=' ')
        n1+=1


num = int(input("Enter a number to generate : "))
prime(num)
