def lantern(lst):
    num = [0]*10
    for i in range(0, len(lst)-1):
        num[i] = lst[i+1]
    num[6] += lst[0]
    num[8] += lst[0]
    return num

lanternfish = list(map(int, input().split(',')))
countlst = [0]*10
for i in range(300):
    countlst[lanternfish[i]] += 1
for i in range(256):
    countlst = lantern(countlst)
sum = 0
for i in range(10):
    sum += countlst[i]
print(sum)