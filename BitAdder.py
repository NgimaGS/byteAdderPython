import LogicalGates as gate #imports functions from LogicalGates

def byte_adder(a, b, cin):
    output = ""
    #sum value
    for i in range(len(b)-1,-1,-1): #loop 8 times 
        fs = gate.xor_Gate(int(a[i]),int(b[i]))
        sum_val = gate.xor_Gate(fs, cin)
        output += str(sum_val)
        #for carryOver
        fco = gate.and_Gate(int(a[i]),int(b[i]))
        fco2 = gate.and_Gate(fs,cin)
        co = gate.or_Gate(fco, fco2)
        cin = co
        #this is the carry over value
    if cin == 1:
        output += str(cin)
    output = output[::-1] #Reverses the output

    return output
