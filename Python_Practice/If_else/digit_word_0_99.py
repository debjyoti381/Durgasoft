def digit_word(num):
    words_upto_19 = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    words_for_tens = ['','','tweny','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    if num==0:
        return 'zero'
    elif num<20:
        return words_upto_19[num]
    elif num<100:
        return words_for_tens[num//10] + " " + words_upto_19[num%10]
    else:
        return "Please enter a value from 0 - 99"
    
num = int(input("Enter a number between 0-99 : "))
print(digit_word(num))