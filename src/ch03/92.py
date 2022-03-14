n,m,k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]
result = 0

t = m // (k+1)
l = m % (k+1)

result += (first * (k) + second) * t

result += first * l

print(result)