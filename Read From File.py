

namesOccur = {}
categoryOccur = {}
with open('namelist.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        if line.strip() not in namesOccur:
            namesOccur[line.strip()] = 1
        else:
            namesOccur[line.strip()] += 1
        line = open_file.readline()

print(namesOccur)

with open('categories.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        if line.split('/')[2] not in categoryOccur:
            categoryOccur[line.split('/')[2]] = 1
        else:
            categoryOccur[line.split('/')[2]] += 1
        line = open_file.readline()

print("{" + "\n".join("{}: {}".format(k, v) for k, v in categoryOccur.items()) + "}")
