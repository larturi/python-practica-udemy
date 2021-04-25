import array

arrPrimos = []

def primos(maximo):
    for n in range(maximo):
        if isPrime(n):
            arrPrimos.append(n)
    print(arrPrimos)

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True 

primos(100000)

