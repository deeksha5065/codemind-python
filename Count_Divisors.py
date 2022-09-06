l,r,k = map(int,input().split())
f = 0
for i in range(l,r+1):
    if i%k==0:
        f+=1
print(f)