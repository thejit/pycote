#효율적인 화폐구성
n,m=2,15
array=[2,3]

d=[10001] * (m+1)
d[0]=0
for i in range(n):
    for j in range(array[i], m+1):
        print('d[j]=', d[j])
        print('d[j-array[i]]=', d[j-array[i]])
        print('array[i]=', array[i])
        if d[j-array[i]] != 1000:
            d[j]=min(d[j],d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])