A = 45
B = 21
r1 = A
r2 = B
s1 = 1
s2 = 0
t1 = 0
t2 = 1

while 1:
    q = r1 // r2
    r=r1-q*r2
    s=s1-q*s2
    t=t1-q*t2
    if r==0:
      x=s2
      y=t2
      break
    r1 = r1
    r2 = r
    s1 = s2
    s2 = s
    t1 = t2
    t2 = t
print("x = ", x, ",y=",y)
print( A,"x + ",B,"y")
print( A*x," + ",B*y)
print((A*x + B*y))
