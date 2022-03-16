#두 배열의 원소 교체
n = 5
k = 3

A = [1,2,5,4,3]
B = [5,5,6,6,5]

a = sorted(A)
b = sorted(B, reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break

print(a)
print(sum(a))
