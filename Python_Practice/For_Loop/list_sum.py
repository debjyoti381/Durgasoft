# WAP to print the sum of numbers in the list 
def sum_list(list):
    sum = 0
    for i in list:
        sum+=i
    print(sum)


list = eval(input("Enter list of number : "))
# sum_list(list)

print(sum(list))