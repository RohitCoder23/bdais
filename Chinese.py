a = [3, 3, 0] 
m = [7, 13, 12]
M = 1
for i in m:
    M = M *i
Mi = [] 
for i in range(len(m)):
    Mi.append(M//m[i])
Minv = []
i = 0
while i < len(m):
     r1 = m[i] 
     r2 = Mi[i] 
     t1 = 0 
     t2 = 1
     MinvA = r1 % r2
     while 1:
          q =  r1 // r2
          r = r1 % r2 
          t = t1 - q* t2
          if r ==1:
               Minv.append(MinvA + t)
               i+=1
               break
          r1 = r2
          r2 = r
          t1 = t2
          t2 = t
X = 0 
for k in range(len(a)):
      X = X + a[k] *Mi[k] * Minv[k]
for j in range(len(a)):
    print("X =",a[j],"%",m[j]) 
print("x is congruent to", X%M)
