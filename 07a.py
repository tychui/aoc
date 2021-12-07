numbers = list(map(int, input().split(',')))
numbers.sort()
median = (len(numbers)-len(numbers)%2)//2
diff = 0
for i in range (len(numbers)):
    diff += abs(numbers[i]-numbers[median])
print(diff)
