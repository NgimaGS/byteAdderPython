import conversion as BC #import functions from module conversion
import BitAdder as BAdder #import functions from module BitAdder

def BinaryAdder():
    print("-----Binary Adder-----")
    execute = False #Condition for the main loop to continue
    while execute == False:
        complete = False #condition for the input loop to continue
        while complete == False:
            try:
                x = int(input("Enter First Number: ")) #input integer value
               
                cin = 0
                if x > 255 or x < 0:
                    print("The entered Number should be in between 0 and 255")
                else:
                    complete = True
            except:
                print("The entered value is Incorrect") #for Exception when the user inputs alphabets or symbols
        complete = False
        while complete == False:
            try:
                y = int(input("Enter Second Number: "))
                if y > 255 or y<0:
                    print("The entered Number should be in between 0 and 255")
                else:
                    complete = True
            except:
                print("The entered value is Incorrect") #for exception when the user inputs alphabets or symbols
        BinaryX = BC.decimalToBinary(x) #binary value of x in string
        BinaryY = BC.decimalToBinary(y) #binary value of Y in string
        print(f"Binary Value of 1st number: {BinaryX}")
        print(f"Binary Value of 2nd Number: {BinaryY}")
        value = ""
        value = BAdder.byte_adder(str(BinaryX),str(BinaryY),cin) #Function for adding two 8-digit binary numbers
        print(f"Sum: {value}")
        exe = input("Press Enter to Continue/Enter N to Exit: ") #input for asking the user to continue
        exe = exe.upper() #changing the input given by the user to uppercase if the input taken is in lower case
        if exe == "N":
            execute = True
            print("/.....Exiting the Program...../")

            
BinaryAdder() #calling function Binary adder

