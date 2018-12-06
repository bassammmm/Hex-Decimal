

def dec_hex(decimal):
    q = decimal
    hexa = []
    while q!=0:
        r = q%16
        if r==10:
            hexa.append('A')
        elif r==11:
            hexa.append('B')
        elif r==12:
            hexa.append('C')
        elif r==13:
            hexa.append('D')
        elif r==14:
            hexa.append('E')
        elif r==15:
            hexa.append('F')
        else:
            hexa.append(str(r))
        q = q//16
    hexa.reverse()
    hexa = ''.join(hexa)
    print("The binary value is :",hexa)
    
def hex_dec(hexadecimal):
    hex_lst=list(hexadecimal)
    hex_lst.reverse()
    sum=0
    for vale in range(len(hex_lst)):
        if hex_lst[vale]=='A' or hex_lst[vale]=='a':
            hex_lst[vale]=10
        elif hex_lst[vale]=='B' or hex_lst[vale]=='b':
            hex_lst[vale]=11
        elif hex_lst[vale]=='C' or hex_lst[vale]=='c':
            hex_lst[vale]=12
        elif hex_lst[vale]=='D' or hex_lst[vale]=='d':
            hex_lst[vale]=13
        elif hex_lst[vale]=='E' or hex_lst[vale]=='e':
            hex_lst[vale]=14
        elif hex_lst[vale]=='F' or hex_lst[vale]=='f':
            hex_lst[vale]=15
        sum += (16**vale)*int(hex_lst[vale])
    print(sum)


decimal = int(input("Please input a number to convert it to Hexadeciaml value:"))
dec_hex(decimal)
hexadecimal = input("Please input a Hexadecimal number to convert it to Decimal value:")
hex_dec(hexadecimal)
                     
    
    








