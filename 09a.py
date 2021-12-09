risk = 0
numlst = []
for i in range(100):
    row = list(map(int, list(input())))
    numlst.append(row)
i = 0
for j in range(1, len(numlst[i])-1):
    if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i+1][j]:
        risk += 1
        risk += numlst[i][j]
j = 0
if numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i+1][j]:
    risk += 1
    risk += numlst[i][j]
j = len(numlst[i])-1
if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i+1][j]:
    risk += 1
    risk += numlst[i][j]
for i in range(1, 99):
    for j in range(1, len(numlst[i])-1):
        if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i+1][j] and numlst[i][j] < numlst[i-1][j]:
            risk += 1
            risk += numlst[i][j]
    j = 0
    if numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i+1][j] and numlst[i][j] < numlst[i-1][j]:
        risk += 1
        risk += numlst[i][j]
    j = len(numlst[i])-1
    if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i+1][j] and numlst[i][j] < numlst[i-1][j]:
        risk += 1
        risk += numlst[i][j]
i = 99
for j in range(1, len(numlst[i])-1):
    if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i-1][j]:
        risk += 1
        risk += numlst[i][j]
j = 0
if numlst[i][j] < numlst[i][j+1] and numlst[i][j] < numlst[i-1][j]:
    risk += 1
    risk += numlst[i][j]
j = len(numlst[i])-1
if numlst[i][j] < numlst[i][j-1] and numlst[i][j] < numlst[i-1][j]:
    risk += 1
    risk += numlst[i][j]
print(risk)