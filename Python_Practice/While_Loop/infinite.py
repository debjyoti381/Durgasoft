import random
def Game():
    while True:
        n = random.randint(1,100)
        print(n)
        num = int(input("Enter a number between 1 to 100 to guess : "))
        if n==num:
            print("Your guess is correct")
            choice = input('Do you want to continue : [y/n] ')
            if choice.lower() == 'y':
                pass
            else:
                print("Thans for paying...")
                break
        else:
            print("Wrong guess !!! Try again")


Game()