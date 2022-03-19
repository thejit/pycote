#바닥공사
n=3
d=[0]*1001
d[1]=1
d[2]=3
for i in range(3,n+1):
    print('d[i-1]=', d[i-1] )
    print('d[i-2]=', d[i-2] )
    d[i]=(d[i-1]+2 * d[i-2]) % 796796

print(d[n])
