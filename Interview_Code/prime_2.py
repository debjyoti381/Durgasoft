# WAP to generate first n prime numbers?
def prime(n):
    count = 0
    n1 = 2
    while True:
        is_prime = True
        for i in range(2,n1//2+1):
            if n1 % i == 0:
                is_prime = False
                break
        if is_prime == True:
            print(n1,end=' ')
            count+=1
        if count == n:
            break
        n1+=1

num = int(input("Enter n number to generate : "))
prime(num)