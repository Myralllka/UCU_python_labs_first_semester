# from CMU 15-112
# http://www.cs.cmu.edu/~112

# Sieve of Eratosthenes

# This function returns a list of prime numbers
# up to n (inclusive), using the Sieve of Eratosthenes.
# See http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def sieve(n):
    isPrime = [ True ] * (n+1) # assume all are prime to start
    isPrime[0] = isPrime[1] = False # except 0 and 1, of course
    primes = [ ]
    for prime in range(n+1):
        if (isPrime[prime] == True):
            # we found a prime, so add it to our result
            primes.append(prime)
            # and mark all its multiples as not prime
            for multiple in range(2*prime, n+1, prime):
                isPrime[multiple] = False
    return primes

print(sieve(100))
