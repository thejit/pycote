#개미전사
n=4
k=[1,3,1,5]

d=[0]*100
d[0]=k[0]
d[1]=max(k[0],k[1])
for i in range(2, n):
    print('d[i-1]=', d[i-1] )
    print('d[i-2]=', d[i-2] )
    print('k[i]=', k[i] )
    d[i]=max(d[i-1],d[i-2]+k[i])
print(d[n-1])