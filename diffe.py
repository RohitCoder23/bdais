p=int(input("Enter a Prime number: ")) #prime number
g=int(input("Enter primitive root: ")) #primitve root
print("p=",p)
print("g=",g)
SA=9 # Private key a
SB=4 #private key b
print("1st Private Key:",SA)
print("2nd Private Key:",SB)
TA=(g**SA)%p #generated key
TB=(g**SB)%p
Ka=(TB**SA)%p # Secret key 1
Kb=(TA**SB)%p # Secret key 2
print("1st Secret key is : ",Ka)
print('2nd Secret key is :',Kb)
