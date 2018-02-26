

n = 10
arr = []
for i in range(1, n+1):
    arr.append(i)

arr.append(3)
sumOfSeries = ((n+1)*n)/2
sumOfArr = sum(arr)
print(int(sumOfArr - sumOfSeries))