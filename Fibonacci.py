
def fibonacci(num):
    result = [0, 1]
    for i in range(2, num+1):
        result.append(result[i-2] + result[i-1])
    result.remove(0)
    return result


inp = int(input("enter a number"))
res = fibonacci(inp)
print(res)