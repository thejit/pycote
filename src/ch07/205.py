#떡볶이 떡 만들기
n, m = 4, 6
h = [19,15,10,17]

start=0
end=max(h)

result=0
while(start<=end):
    total=0
    mid = (start+end) // 2
    for x in h:
        if x>mid:
            total += x-mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
