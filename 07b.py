from math import floor

numbers = list(map(int, input().split(',')))
numbers.sort()
diff = 0
totalsum = 0
for i in range (len(numbers)):
    totalsum += numbers[i]
middle = floor(totalsum/len(numbers))
for i in range(len(numbers)):
    k = abs(middle-numbers[i])
    for j in range(1, k+1):
        diff += j   
print(diff)
