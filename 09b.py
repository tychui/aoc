def risk(numlst):
    risklst = []
    i = 0
    for j in range(1, len(numlst[i])-1):
        if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i+1][j]:
            risklst.append((i, j))
    j = 0
    if numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i+1][j]:
        risklst.append((i, j))
    j = len(numlst[i])-1
    if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i+1][j]:
        risklst.append((i, j))
    for i in range(1, 99):
        for j in range(1, len(numlst[i])-1):
            if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i+1][j] and numlst[i][j] < numlst[i-1][j]:
                risklst.append((i, j))
        j = 0
        if numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i+1][j] and numlst[i][j] < numlst[i-1][j]:
            risklst.append((i, j))
        j = len(numlst[i])-1
        if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i+1][j] and numlst[i][j] < numlst[i-1][j]:
            risklst.append((i, j))
    i = 99
    for j in range(1, len(numlst[i])-1):
        if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i-1][j]:
            risklst.append((i, j))
    j = 0
    if numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i-1][j]:
        risklst.append((i, j))
    j = len(numlst[i])-1
    if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i-1][j]:
        risklst.append((i, j))
    return risklst
risklst = []
numlst = []
def bfs(numlst, risklst):
    pass
for i in range(100):
    row = list(map(int, list(input())))
    numlst.append(row)
risklst = risk(numlst)
for i in range(100):
    for j in range(100):
        if numlst[i][j] == 9:
            print(' ', end='')
        else:
            print(numlst[i][j], end='')
    print()
print(risklst)
