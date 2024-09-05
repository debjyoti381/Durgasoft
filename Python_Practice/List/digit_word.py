def digit_word(lst):
    l = ['zero','one','two','three','four','five','six','seven','eight','nine']
    if lst>=0 and lst <10:
        print(f"{lst} in word is '{l[lst]}'")
    else:
        print("Please enter a number between 0-9")
n =int(input("Enter a number between0-9 : "))
digit_word(n)