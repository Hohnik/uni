from collections import Counter

def main():

    primes = []
    for i in range(2,10001):
        primes.append(smallest_factor(i))

    primes_counter = Counter(primes)
    for prime, count in primes_counter.most_common():
        if count > 1 :
            print(f"{prime}: {count}") 
    




def is_prime(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    return isPrime

def smallest_factor(n:int):
    if(is_prime(n)):
        return n
    
    for i in reversed(range(2, n)):
        if n % i == 0:
            return smallest_factor(int(n/i))
            
def test_smallest_factor():
    assert smallest_factor(2) == 2
    assert smallest_factor(4) == 2
    assert smallest_factor(21) == 3
test_smallest_factor()

if __name__ == "__main__":
    main()