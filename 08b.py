def pattern(patternlst):
    patlst = ['']*10
    for i in range(len(patternlst)):
        if len(patternlst[i]) == 2:
            patlst[1] = patternlst[i]
        if len(patternlst[i]) == 3:
            patlst[7] = patternlst[i]
        if len(patternlst[i]) == 4:
            patlst[4] = patternlst[i]
        if len(patternlst[i]) == 7:
            patlst[8] = patternlst[i]
        if len(patternlst[i]) == 6 and (patlst[1][0] not in patternlst[i] or patlst[1][1] not in patternlst[i]):
            patlst[6] = patternlst[i]
        if len(patternlst[i]) == 5 and (patlst[1][0] in patternlst[i] and patlst[1][1] in patternlst[i]):
            patlst[3] = patternlst[i]
    return patlst

total = 0
for i in range(200):
    patternlst, output = input().split('|')
    patternlst = list(patternlst.split())
    patternlst = pattern(patternlst)
    outputlst = output.split()
    num = 0
    for i in len(outputlst):
        for j in len(patternlst):
            if outputlst[i] == patternlst[j]:
                num += (10**(3-i))*(j+1)
    total += num
print(total)
