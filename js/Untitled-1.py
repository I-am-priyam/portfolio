n,m=map(int,input().split(" "))
k=n
for i in range(n+1):
    for j in range(i+1):
        print(k," ",end="",)
    k+=1
    print("")
for i in range(n,1):
