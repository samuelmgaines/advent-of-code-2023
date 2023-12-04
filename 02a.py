line = input()
ans=0
while line != "done":

    # separate hand and game info
    hands = line.split(';')
    for i in range(len(hands)):
        hands[i] = hands[i].split(',')
    [handInfo, hands[0][0]] = hands[0][0].split(':')
    id = int(handInfo[5:])

    # check if each hand is valid
    d = {'red': 12, 'green': 13, 'blue': 14}
    isValidGame = True
    for hand in hands:
        for value in hand:
            [value, color] = value.split()
            value = int(value)
            if value > d[color]:
                isValidGame = False
                break
        if not isValidGame: break
    
    if isValidGame: ans += id
    line = input()

print(ans)