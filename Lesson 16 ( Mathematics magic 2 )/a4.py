def primenum(num):
    if num < 2:
        print("There are no prime numbers less than 2.")
        return

    prime = [True for i in range(num)]
    p = 2
    while (p * p < num):
        if prime[p]:
            for i in range(p * p, num, p):
                prime[i] = False
        p += 1

    for p in range(2, num):
        if prime[p]:
            print(p, end=' ')

# Print primes less than 100
primenum(100)
