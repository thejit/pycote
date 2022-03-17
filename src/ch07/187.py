#순차 탐색
def sequential_search(target ,array):
    for i in range(len(array)):
        if array[i] == target:
            return i+1

target = 'd'
array = ['a', 'b', 'c', 'd', 'e']
print(sequential_search(target, array))
