n = input()
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    next_y = row + step[0]
    next_x = col + step[1]
    if next_y>=1 and next_y<=8 and next_x>=1 and next_x<=8:
        result += 1

print(result)
