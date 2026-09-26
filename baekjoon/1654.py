k,n = map(int,input().split())
arr = [int(input()) for _ in range(k)]

s,e = 1,max(arr)+1
while e-s!=1:
    cm = (s+e)//2
    if sum(x//cm for x in arr)<n:
        e = cm
    else:
        s = cm

print(s)


