line = input()
sum = 0
while line != "done":
    i = 0
    while True:
        if line[i].isdigit():
            sum += int(line[i]) * 10
            break
        i += 1
    i = len(line)-1
    while True:
        if line[i].isdigit():
            sum += int(line[i])
            break
        i -= 1
    line = input()
print(sum)
