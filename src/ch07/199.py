#부품찾기 - 계수 정렬

n = 5
array = [0] * 1000001
p = [8,3,7,9,2]
for i in p:
    array[i] += 1

m = 3
r = [5,7,9]
for i in r:
    if array[i] == 0:
        print(i, ' = no ')
    else:
        print(i, ' = yes ')
