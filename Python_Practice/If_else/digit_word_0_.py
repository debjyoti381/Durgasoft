def digit_word(num):
    words_upto_19 = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    words_for_tens = ['','','tweny','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    hundreds = 'hundred'
    thousand = 'thousand'
    x = num % 100
    y = num % 1000
    if num==0:
        return 'zero'
    elif num<20:
        return words_upto_19[num]
    elif num<100:
        return words_for_tens[num//10] + " " + words_upto_19[num%10]
    elif num<1000:
        return words_upto_19[num//100] + " " + hundreds + " " + words_for_tens[x//10] + " " + words_upto_19[x % 10]
    elif num<=10000:
        return words_upto_19[num//1000] + " " + thousand + (" " + words_upto_19[y//100] + " " + hundreds if y>=100 else '') + (" " + words_for_tens[y%100//10] ) + " " + words_upto_19[(y%100)%10]
    else :
        return ("This can only do upto 10000")
num = int(input("Enter a number : "))
print(digit_word(num))