g_break_count = 0
def recursive_func():
    global g_break_count
    if g_break_count > 5:
        return
    print('재귀 함수 호출')
    g_break_count += 1
    recursive_func()

recursive_func()