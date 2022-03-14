n, m = map(int, input().split())

result = 0
for row in range(n):
    col = list(map(int, input().split()))
    min_value = min(col)
    result = max(result,min_value)

print(result)