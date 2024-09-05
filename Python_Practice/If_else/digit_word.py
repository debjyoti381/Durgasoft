# WAP to take a single number from the user and plot it value in English Word.

def convert_to_words(num):
    ones = ("","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen")
    tens = ("","","tweenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
    thousands = ("","thousand")

    if num==0:
        print("zero")
    
    def convert_hunderds(n):
        if n<20:
            return ones[n]
        elif n<100:
            return tens[n//10] + ('' if n%10 == 0 else '-' + ones[n%10])
        else:
            return ones[n//100] + ' hundred ' + ('' if n%100 == 0 else ' and ' + convert_hunderds(n%100))
        
    result = []
    if num >=1000:
        result.append(convert_hunderds(num//1000) + ' thousand')
        num %= 1000
    if num>0:
        result.append(convert_hunderds(num))

    return ' '.join(result)

num = int(input("Enter a number to convert : "))
words = convert_to_words(num)
print(words)