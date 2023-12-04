def getNum(row, c):
    l = r = c
    while l > 0 and scm[row][l-1].isdigit(): l -= 1
    while r < numCols-1 and scm[row][r+1].isdigit(): r += 1
    return int(scm[row][l:r+1])


def rowOfThree(r, c, adjNums):
    if c == 0:
        if scm[r][c].isdigit(): adjNums.append(getNum(r, c))
        elif scm[r][c+1].isdigit(): adjNums.append(getNum(r, c+1))
    elif c == numCols-1:
        if scm[r][c-1].isdigit(): adjNums.append(getNum(r, c-1))
        elif scm[r][c].isdigit(): adjNums.append(getNum(r, c))
    else:
        if scm[r][c-1].isdigit() and not scm[r][c].isdigit() and scm[r][c+1].isdigit():
            adjNums.append(getNum(r, c-1))
            adjNums.append(getNum(r, c+1))
        elif scm[r][c-1].isdigit():
            adjNums.append(getNum(r, c-1))
        elif scm[r][c].isdigit():
            adjNums.append(getNum(r, c))
        elif scm[r][c+1].isdigit():
            adjNums.append(getNum(r, c+1))


def getGearRatio(r, c):
    adjNums = []
    if r != 0: rowOfThree(r-1, c, adjNums)
    if r != numRows-1: rowOfThree(r+1, c, adjNums)
    if c != 0 and scm[r][c-1].isdigit(): adjNums.append(getNum(r, c-1))
    if c != numCols-1 and scm[r][c+1].isdigit(): adjNums.append(getNum(r, c+1))
    if len(adjNums) >= 2:
        p = 1
        print("nums of ", end="")
        for num in adjNums:
            p *= num
            print (str(num) + ", ", end="")
        print()
        return p
    else: return 0


scm = []
row = input()
while row != "done":
    scm.append(row)
    row = input()
numRows, numCols = len(scm), len(scm[0])

sum = 0
for rowNum, row in enumerate(scm):
    for i, c in enumerate(row):
        if c == '*': sum += getGearRatio(rowNum, i)

print(sum)