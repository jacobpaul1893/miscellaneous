def intarr(n, a):
  if n%2 == 1:
    b = a[int((n-1)/2)]
    for j in range(n+1):
      if a[j]==0:
        a.insert(j+1, b)
    
  elif n%2 == 0:
    b = (a[int((n-2)/2)] + a[int(n/2)])
    for k in range(n+1):
      if a[k] == 0:
        a.insert(k+1, b)
   return a
  




T = int(input().strip())

for i in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    r = intarr(n, a)
    print(r)

