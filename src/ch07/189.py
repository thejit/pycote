#이진 탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


target = 'd'
array = ['a', 'b', 'c', 'd', 'e']
result = binary_search(array, target, 0, 4)
if result == None:
    print('None')
else:
    print(result+1)
