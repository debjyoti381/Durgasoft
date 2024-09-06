# WAP to print Inverted pyramid pattern using * symbol
# Method 1
def pyramid(n):
    for i in range(n):
        print(' '*i+ '* '*(n-i))
        
num = int(input("Enter a number : "))
pyramid(num)
