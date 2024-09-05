# Paindrome String :
# 1. Split Method () :

def Palindrome(s):
    temp = s[::-1]
    if s == temp:
        print(f"'{s}' is Palindrome")
    else:
        print(f"'{s}' is Not a Palindrome")

# s = input("Enter a string : ")
# Palindrome(s)

# 2. By using indexing / using for loop

def Palindrome2(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-i-1]:
            return False
    return True

# s = 'mauka'
# print(Palindrome2(s))

# 3. By using inbuilt function :

def Palindrome3(s):
    temp = ''.join(reversed(s))
    if s == temp:
        print(f"{s} is Palindrome")
    else:
        print(f"{s} is not a Palindrome")

Palindrome3('nitin')
