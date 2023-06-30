def twoSum(tupl,n):
    list = []
    i = 0
    j = len(tupl)-1
    while(i<j):
        if tupl[i]+tupl[j] > n:
            j -= 1
        if tupl[i]+tupl[j] < n:
            i += 1
        if tupl[i]+tupl[j] == n:
            list.append(i)
            list.append(j)
            break

    return list

tupl = [2, 7, 11, 15]
n = 9

print(twoSum(tupl,n))