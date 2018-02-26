

def removeDuplicates(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result


names = ["Michele", "Robin", "Sara", "Michele"]

print(removeDuplicates(names))