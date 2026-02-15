def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(start, end):
    count = 0
    for i in range(start, end+1):
        if is_prime(i):
            count += 1
    return count

print(count_primes(14,52))