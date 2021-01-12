def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


number = int(input("Enter an integer (2 or greater) :"))
if number <= 2:
    print("Error! Please enter a number greater than 2")
else:
    print("The prime factors of", number, "are:", prime_factors(number))
