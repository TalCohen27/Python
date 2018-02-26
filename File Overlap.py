

def extractLinesFromFile(file_name):
    result = set()
    with open(file_name, 'r') as open_file:
        line = open_file.readline()
        while line:
            result.add(int(line.strip()))
            line = open_file.readline()
    return result


print(extractLinesFromFile('happy.txt').intersection(extractLinesFromFile('primes.txt')))
