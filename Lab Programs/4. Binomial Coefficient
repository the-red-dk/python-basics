#Binomial Coefficient

def fact(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res

def ncr(n, r):
    return (fact(n) / (fact(n-r) * fact(r)))

print("Enter values for Binomial Coefficient: ")
n = int(input("N: "))
r = int(input("R: "))
res = ncr(n, r)

print(res)
