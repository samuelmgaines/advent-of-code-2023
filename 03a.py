def isSymbol(c):
    return (not c.isdigit()) and c != '.'


def isAdjacentSymbol(rowNum, start, stop):
    lastSpot = len(scm[rowNum])-1
    if start != 0 and isSymbol(scm[rowNum][start-1]): return True
    if stop != lastSpot and isSymbol(scm[rowNum][stop+1]): return True
    if rowNum != 0:
        for i in range(start-1, stop+2):
            if i >= 0 and i <= lastSpot and isSymbol(scm[rowNum-1][i]): return True
    if rowNum != len(scm)-1:
        for i in range(start-1, stop+2):
            if i >= 0 and i <= lastSpot and isSymbol(scm[rowNum+1][i]): return True
    return False


scm = []
row = input()
while row != "done":
    scm.append(row)
    row = input()

sum = 0
for rowNum, row in enumerate(scm):
    inANumber = False
    for i, c in enumerate(row):
        if inANumber:
            if c.isdigit():
                currNumber = currNumber*10 + int(c)
                stop = i
            else:
                if isAdjacentSymbol(rowNum, start, stop):
                    sum += currNumber
                inANumber = False
        else:
            if c.isdigit():
                inANumber = True
                currNumber = int(c)
                start = stop = i
    if inANumber and isAdjacentSymbol(rowNum, start, stop):
        sum += currNumber


print(sum)