def pattern(patternlst):
    patlst = ['']*10
    for i in range(len(patternlst)):
        if len(patternlst[i]) == 2:
            patlst[1] = "".join(sorted(patternlst[i]))
        elif len(patternlst[i]) == 3:
            patlst[7] = "".join(sorted(patternlst[i]))
        elif len(patternlst[i]) == 4:
            patlst[4] = "".join(sorted(patternlst[i]))
        elif len(patternlst[i]) == 7:
            patlst[8] = "".join(sorted(patternlst[i]))
    for i in range(len(patternlst)):
        if "".join(sorted(patternlst[i])) in patlst:
            continue
        elif len(patternlst[i]) == 6:
            if patlst[1][0] not in patternlst[i] or patlst[1][1] not in patternlst[i]:
                patlst[6] = "".join(sorted(patternlst[i]))
            else:
                status = True
                for j in range (len(patlst[4])):
                    if patlst[4][j] not in patternlst[i]:
                        status = False
                if status == True:
                    patlst[9] = "".join(sorted(patternlst[i])) 
                else:
                    patlst[0] = "".join(sorted(patternlst[i]))
    for i in range(len(patternlst)):
        patternlst[i] = "".join(sorted(patternlst[i]))
        status = True
        for j in range (len(patlst)):
            if patternlst[i] != patlst[j]:
                status = False
        if status == True:
            continue
        elif len(patternlst[i]) == 5:
            if (patlst[1][0] in patternlst[i]) and (patlst[1][1] in patternlst[i]):
                patlst[3] = "".join(sorted(patternlst[i]))
            else:
                total = []
                for j in range(len(patternlst[i])):
                    total.append(patternlst[i][j])
                for j in range(len(patlst[1])):
                    total.append(patlst[1][j])
                total.sort()
                k = 0
                for j in range(1, len(total)):
                    if total[j] == total[j-1]:
                        k = j-1
                total.remove(total[k])
                total = "".join(total)
                statusn = True
                for j in range(len(total)):
                    if total[j] != patlst[9][j]:
                        statusn = False
                if statusn == True:
                    patlst[5] = "".join(sorted(patternlst[i]))
                else:
                    patlst[2] = "".join(sorted(patternlst[i])) 
    return patlst

total = 0
for i in range(200):
    patternlst, output = input().split('|')
    patternlst = list(patternlst.split())
    patternlst = pattern(patternlst)
    outputlst = output.split()
    num = 0
    for i in range (len(outputlst)):
        outputlst[i] = "".join(sorted(outputlst[i]))
        for j in range (len(patternlst)):
            if outputlst[i] == patternlst[j]:
                num += (10**(3-i))*j
    total += num
print(total)
