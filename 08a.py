count = 0
for i in range(200):
    pattern, output = input().split('|')
    outputlst = output.split()
    for word in outputlst:
        if len(word) == 2  or len(word) == 3 or len(word) == 4 or len(word) == 7:
            count += 1
print(count)