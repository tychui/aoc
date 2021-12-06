def lantern(lst):
    for i in range(len(lst)):
        lst[i] -= 1
        if lst[i] == -1:
            lst[i] += 7
            lst.append(8)
    return lst

lanternfish = list(map(int, input().split(',')))
for i in range(80):
    lantern(lanternfish)
print(len(lanternfish))