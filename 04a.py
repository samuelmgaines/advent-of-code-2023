def update(p):
    if p == 0: return 1
    return p*2


line = input()
ans = 0
while line != "done":
    [winningLine, yourLine] = line.split('|')
    winningLine = winningLine.split(':')[1]
    winningNums, yourNums = set(), set()
    for num in winningLine.split(): winningNums.add(int(num))
    for num in yourLine.split(): yourNums.add(int(num))

    p = 0
    for num in yourNums:
        if num in winningNums: p = update(p)
    ans += p
    line = input()

print(ans)