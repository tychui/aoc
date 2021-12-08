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
        if patlst[1] != '':
            if len(patternlst[i]) == 6 and (patlst[1][0] not in patternlst[i] or patlst[1][1] not in patternlst[i]):
                patlst[6] = "".join(sorted(patternlst[i]))
            elif len(patternlst[i]) == 5 and (patlst[1][0] in patternlst[i] and patlst[1][1] in patternlst[i]):
                patlst[3] = "".join(sorted(patternlst[i]))
        elif len(patternlst[i]) == 6:
            if patlst[4] != '':
                status = True
                for j in range (len(patlst[4])):
                    if patlst[4][j] not in patternlst[i]:
                        status = False
                if status == True:
                    patlst[9] = "".join(sorted(patternlst[i])) 
                else:
                    patlst[0] = "".join(sorted(patternlst[i]))
        elif len(patternlst[i]) == 5:
            if patlst[1] != '':
                total = "".join(patlst[1],patternlst[i])
                total = "".join(sorted(total))
                for j in range(1, len(total)):
                    if total[j] == total[j-1]:
                        total.remove(total[j])
                if total == patlst[9]:
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
                num += (10**(3-i))*(j+1)
    total += num
print(total)
