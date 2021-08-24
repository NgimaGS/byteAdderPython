#Gates for BitAdder

#AND Gate 
def and_Gate(a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0

#OR Gate
def or_Gate(a,b):
    if a==0 and b==0:
        return 0
    else:
        return 1

#XOR Gate
def xor_Gate(a,b):
    if (a==1 and b==1) or (a==0 and b==0):
        return 0
    else:
        return 1

    
