def calulateSumAndAverage(list) : 
    tosum = sum(list)
    average = tosum/len(list)
    return tosum, average    

list = [10,20,30,40]

sum, average = calulateSumAndAverage(list)

print(f"Sum = {sum}, Average = {average}")