# WAP a program to check a number prime or not 
def prime(n):
    if n<=1:
        print(f"{n} is not a prime number")
    else:
        is_prime = True
        for i in range(2,n//2+1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime == True:
            print(f"{n} is prime a number")
        else:
            print(f"{n} is not prime a number")
            

num=int(input("Enter a number to check prime or not : "))
prime(num)