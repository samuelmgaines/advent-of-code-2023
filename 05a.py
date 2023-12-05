def addMap(line, d):
    [dest, src, r] = map(int, line.split())
    d[(src, r)] = dest


def readMap(src, d):
    for key in d:
        if src >= key[0] and src < key[0] + key[1]:
            return d[key] + (src - key[0])
    return src


seeds = map(int, input().split()[1:])
input()

maps = []

line = input()
while line != "done":
    maps.append({})
    line2 = input()
    while line2 != "" and line2 != "done":
        addMap(line2, maps[-1])
        line2 = input()
    if line2 == "done": break
    line = input()

locs = set()
for seed in seeds:
    src = seed
    for mapper in maps:
        src = readMap(src, mapper)
    locs.add(src)

print(min(locs))