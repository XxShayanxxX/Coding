def romanToInt(romaninput):

    #All roman numebr with numeric values 
    roman = {"M" : 1000,"D" : 500,"C" : 100,"L" : 50,"X" : 10,"V" : 5,"I" : 1}
    #result
    resultinteger = 0 

    for i in range(0, len(romaninput)- 1):
        if roman[romaninput[i]] < roman[romaninput[i + 1]]:
            resultinteger -= roman[romaninput[i]]
        else:
            resultinteger += roman[romaninput[i]]
    return resultinteger + roman[romaninput[- 1]]

roman1 =  input("Enter a roman number:")

print("Interger value equivalent of roman number is: ", romanToInt(roman1))