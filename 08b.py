def pattern(patternlst):
    pass

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
