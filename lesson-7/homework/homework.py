1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

2
def digit_sum(k):
    total = 0
    while k > 0:
        total += k % 10  
        k //= 10        
    return total

3
def powers_of_two(N):
    i = 1
    while i <= N:
        print(i, end=' ')
        i *= 2
      
def powers_of_two(N):
    i = 2
    while i <= N:
        print(i, end=' ')
        i *= 2

