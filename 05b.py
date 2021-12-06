def lantern(n, day):
    count = 0
    return count

lanternfish = list(map(int, input().split(',')))
count = 0
for i in range(len(lanternfish)):
    count += lantern(lanternfish[i], 0)
print(count)
