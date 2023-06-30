def factorial(n) : 
    f = 1
    for i in range(2, n+1):
        f += i
    return f

n = 5
print(f"Factorial of {n} is: {factorial(n)}")