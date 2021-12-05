def lines(lst, oldx, oldy, newx, newy):
    if oldx != newx and oldy != newy:
        if oldx > newx:
            tempx = oldx
            oldx = newx
            newx = tempx
            tempy = oldy
            oldy = newy
            newy = tempy
        count = 0
        for i in range(oldx, newx+1):
            lst[i][oldy+count] += 1
            if oldy > newy:
                count -= 1
            else:
                count += 1
    elif oldx == newx:
        if newy < oldy:
            temp = oldy
            oldy = newy
            newy = temp
        for i in range(oldy, newy+1):
            if lst[oldx][i] == 0:
                lst[oldx][i] = 1
            else:
                lst[oldx][i] = lst[oldx][i]+1
    elif oldy == newy:
        if newx < oldx:
            temp = oldx
            oldx = newx
            newx = temp
        for i in range(oldx, newx+1):
            if lst[i][oldy] == 0:
                lst[i][oldy] = 1
            else:
                lst[i][oldy] = lst[i][oldy]+1
    return lst

diagram = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    diagram.append(row)

for i in range(500):
    old, arrow, new = input().split()
    oldx, oldy = map(int, old.split(','))
    newx, newy = map(int, new.split(','))
    diagram = lines(diagram, oldx, oldy, newx, newy)
count = 0
for i in range(1000):
    for j in range(1000):
        if diagram[i][j] >= 2:
            count += 1
print(count)