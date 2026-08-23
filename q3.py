def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:                  # This else corresponds to the for loop, not the if statement. It executes only if the loop wasn't broken, meaning no divisors were found.   
        return True

    return False


def main():
    n = int(input())

    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(str(num))

    print(" ".join(primes))


if __name__ == "__main__":
    main()