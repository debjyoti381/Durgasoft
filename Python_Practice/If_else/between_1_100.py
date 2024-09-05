# Write a program to check a number between 1 and 100 or Not?

def one_100(n):
    if n>=1 and n<=100:
        print(f"{n} is between 1 and 100")
    else:
        print(f"{n} is not between 1 and 100")

num = int(input("Enter a number : "))
one_100(num)