n = int(input())
a = list(input().split())

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direct_types = ['L', 'R', 'U', 'D']

for arrow in a:
    for i in range(len(direct_types)):
        if arrow == direct_types[i]:
            next_x = x + dx[i]
            next_y = y + dy[i]
    if next_x < 1 or next_y < 1 or next_x > n or next_y > n:
        continue
    x, y = next_x, next_y
    """_summary_
for arrow in a:
    if arrow == 'L' and y > 1:
        y -= 1
    elif arrow == 'R' and y < n:
        y += 1
    elif arrow == 'U' and x > 1:
        x -= 1
    elif arrow == 'D' and x < n:
        x += 1

    """
print(x, y)

