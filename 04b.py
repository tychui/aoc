order = list(map(int, input().split(',')))
sum = [[]*10]*100
def remove(gameboard, number):
    for i in range(100):
        for j in range(5):
            for k in range(5):
                if gameboard[i][j][k] == number:
                    gameboard[i][j][k] = 100
    return gameboard

def bingo(board):
    for i in range(5):
        sum = 0
        for j in range(5):
            sum += board[i][j]
        if sum == 500:
            return True
    for i in range(5):
        sum = 0
        for j in range(5):
            sum += board[j][i]
        if sum == 500:
            return True
    return False

def sumof(board):
    total = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != 100:
                total += board[i][j]
    return total

gameboard = []
for i in range(100):
    k = []
    for j in range(6):
        if j == 0:
            l = input()
        else:
            k.append(list(map(int, input().split())))
    gameboard.append(k)

status = [False]*100
for i in range(97):
    gameboard = remove(gameboard, order[i])
    for j in range(100):
        bing = bingo(gameboard[j])
        if bing == True and status[j] == False:
            sum = sumof(gameboard[j])
            print(sum*order[i])
            status[j] = True