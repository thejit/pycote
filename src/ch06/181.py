#성적이 낮은 순서로 학생 출력하기 - 높은
n = 2
array = [('hong', 95), ('lee', 77)]

result = sorted(array, key=lambda i: i[1], reverse=True)

for i in result:
    print(i[0], end=' ')
print(' ')