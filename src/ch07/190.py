#이진 탐색 (반복)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid+1
    return None

target = 'e'
array = ['a', 'b', 'c', 'd', 'e']
result = binary_search(array, target, 0, 4)
if result == None:
    print('None')
else:
    print(result+1)
