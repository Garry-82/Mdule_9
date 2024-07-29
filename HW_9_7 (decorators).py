def is_prime(func):
    def wrapper(*args):
        summ = func(*args)
        if isPrime(summ) == True:
            print("Простое")
            return summ
        else:
            print("Составное")
            return summ
    return wrapper
@is_prime
def sum_three(*args):
    Sum = 0
    for i in args:
        Sum += i
    return Sum

def isPrime(n):
    k = 2
    while k*k <= n and n % k != 0:
        k += 1
    return (k*k > n)

#for i in range(2,50):
#    if isPrime(i):
#        print(i)

result = sum_three(2, 3, 6)
print(result)

print(sum_three(4,4,4))

