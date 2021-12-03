from math import ceil

def o2(a, k, prevcount):
    if prevcount == 1:
        print(a)
        return
    lst = []
    count = 0
    for s in a:
        count += int(s[k])
    if count >= ceil(prevcount/2):
        for s in a:
            if s[k] == '1':
                lst.append(s)
    else:
        count = prevcount-count
        for s in a:
            if s[k] == '0':
                lst.append(s)
    return o2(lst, k+1, count)

def co2(a, k, prevcount):
    if prevcount == 1:
        print(a)
        return
    lst = []
    count = 0
    for s in a:
        count += int(s[k])
    if count < prevcount//2:
        for s in a:
            if s[k] == '1':
                lst.append(s)
    else:
        count = prevcount-count
        for s in a:
            if s[k] == '0':
                lst.append(s)
    return co2(lst, k+1, count)

a = []
for i in range(1000):
    a.append(input())
k = 0
o2(a, k, 1000)
co2(a, k, 1000)

#O2: 101011101111 (2799)
#CO2: 011001000001 (1601)