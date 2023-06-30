def fibonacci(n) : 
    arr =[]
    if n>= 1:
        arr.append(0)
    if n>=2:
        arr.append(1)
    for i in range(2, n):
        num = arr[i-1]+arr[i-2]
        arr.append(num)

    return arr        

n = 5
print(fibonacci(n))