line = input()
ans = 0
copies = {}
while line != "done":
    # parse input
    [winningLine, yourLine] = line.split('|')
    [gameInfo, winningLine] = winningLine.split(':')
    cardNumber = int(gameInfo.split()[1])
    winningNums, yourNums = set(), set()
    for num in winningLine.split(): winningNums.add(int(num))
    for num in yourLine.split(): yourNums.add(int(num))

    # add how many cards you have
    if cardNumber in copies: numCopies = copies[cardNumber]
    else: numCopies = 0
    numCards = 1 + numCopies
    ans += numCards

    # find amount of winning numbers
    winners = 0
    for num in yourNums:
        if num in winningNums: winners += 1
    
    # create copies
    for i in range(1, winners+1):
        copyNumber = cardNumber + i
        if copyNumber not in copies: copies[copyNumber] = numCards
        else: copies[copyNumber] += numCards
    
    line = input()

print(ans)