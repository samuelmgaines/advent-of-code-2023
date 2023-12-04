line = input()
ans=0
while line != "done":

    # separate hand and game info
    hands = line.split(';')
    for i in range(len(hands)):
        hands[i] = hands[i].split(',')
    handInfo, hands[0][0] = hands[0][0].split(':')[0], hands[0][0].split(':')[1]
    id = int(handInfo[5:])

    # get power of each game
    d = {'red': 0, 'green': 0, 'blue': 0}
    for hand in hands:
        for value in hand:
            [value, color] = value.split()
            value = int(value)
            d[color] = max(d[color], value)
    power = d['red']*d['green']*d['blue']
    ans += power
    line = input()

print(ans)