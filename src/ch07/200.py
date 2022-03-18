#부품찾기 - 집합자료형 찾기
n = 5
p = [8,3,7,9,2]
m = 3
r = [5,7,9]

for i in r:
    if i in p:
        print(i, ' = yes ')
    else:
        print(i, ' = no ')