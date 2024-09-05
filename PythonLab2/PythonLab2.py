def is_prime(number):
    if(number < 0 or number >= 1000): return False #Has no sense because prime numbers only from 0 to 1000
    for i in range(2, number):
        x = number % i
        if  x == 0:
            return False
    return True

print(is_prime(173))
print(is_prime(10))
