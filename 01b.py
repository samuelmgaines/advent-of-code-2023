def findFirstNum(line, numSet):
    firstDigit, i = len(line), 0
    while i < len(line):
        if line[i].isdigit():
            firstDigit = i
            break
        i += 1
    firstWord = len(line)
    for num in numSet:
        if num in line:
            if line.index(num) < firstWord:
                firstWord = line.index(num)
                wordDigit = numSet[num]
    if firstDigit < firstWord:
        return int(line[firstDigit])
    else:
        return wordDigit


line = input()
sum = 0
nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
reversedNums = {'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 'xis': 6, 'neves': 7, 'thgie': 8, 'enin': 9}
while line != "done":
    sum += 10*findFirstNum(line, nums) + findFirstNum(line[::-1], reversedNums)
    i = len(line)-1
    line = input()
print(sum)
