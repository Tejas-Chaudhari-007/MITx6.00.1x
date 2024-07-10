def genPrimes():
    gen_primes = [2]
    x = 2
    while True:
        is_prime = True

        for prev_prime in gen_primes:
            if x % prev_prime == 0:
                is_prime = False
                break

        if is_prime or x == 2:
            gen_primes.append(x)
            yield x

        x += 1

for i, x in enumerate(genPrimes()):
    print(x)

    if i == 15:
        break

