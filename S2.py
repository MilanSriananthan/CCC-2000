streams = int(input())
all = []
for i in range(streams):
    hold = int(input())
    all.append(hold)



while True:
    task = int(input())
    if task == 77:
        break
    elif task == 99:
        point = int(input()) - 1
        percent = int(input())
        first = all[point] * percent // 100
        second = all[point] - first
        all.insert(point, second)
        all.insert(point, first)
        del all[point + 2]
    else:
        point = int(input()) - 1
        total = all[point] + all[point + 1]
        all.insert(point, total)
        del all[point + 1]
        del all[point + 1]

print(*all, sep=" ")