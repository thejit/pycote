#부품찾기
n = 5
p = [8,3,7,9,2]
m = 3
r = [5,7,9]

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

print(sorted(p))
for i in r:
    result = binary_search(sorted(p),i,0,n-1)
    if result == None:
        print(i, ' = no ', result)
    else:
        print(i, ' = yes ', result+1)
