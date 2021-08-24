#for Binary To Decimal Conversion
def binaryToDecimal(Binary):
    decimalValue = 0
    initial = 1
    for i in range(len(Binary)-1,-1,-1):
        decimalValue = decimalValue + initial*Binary[i]
        initial = initial*2
    return decimalValue #returns decimal value of the given Binary digit


#for Decimal to Binary conversion
def decimalToBinary(n):
    temp = []
    Binary = ""
    while n > 0:
        if n%2 != 0:
            temp.append(1) #adds 1 to the list
        else:
            temp.append(0) #adds 0 to the list
        n = int(n/2) #Converts float type value into integer if n/2 contains decimal value
    for i in range(len(temp)-1,-1,-1):
        Binary += str(temp[i])
    if len(Binary) < 8:
        for i in range(len(Binary),8):
            Binary = "0" + Binary #adds 0 if the total length of the numbers is less than 8 digits   
    return Binary #returns Binary digit of the given decimal value
