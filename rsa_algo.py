from decimal import Decimal
def gcd(a,b):
  if b==0:
     return a
  else:
     return gcd(b,a%b)
p = int(input('Enter the value of p = '))
q = int(input('Enter the value of q = '))
no = int(input('Enter the value of text = '))
n = p*q
t = (p-1)*(q-1)
for e in range(2,t):
    if gcd(e,t)== 1:
          break
d=0
while(1):
     if((e*d)%t==1):
         break
     else:
         d=d+1
ctt = Decimal(0)
ctt =pow(no,e)
ct = ctt % n
dtt = Decimal(0)
dtt = pow(ct,d)
dt = dtt % n
print('Enter the value of p = ',p)
print('Enter the value of q = ',q)
print('Enter the value of text = ',no)
print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text= '+str(ct)+' decrypted text = '+str(dt))
