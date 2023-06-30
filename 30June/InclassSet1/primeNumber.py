def prime(n) : 
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 :
            return False         
    return True

n = 12
c = prime(n)
if c:
    print(f"{n} is a prime number.")
else: 
    print(f"{n} is a not prime number.")