#
# - Reduce a fraction to its lowest terms.
#

# Compute the greatest common divisor of two integers.
def gcd(n, m):
    d = min(n, m)
    # Use a while loop to find the greatest common divisor of n and m
    while n % d != 0 or m % d != 0:
        d = d - 1

    return d


# Reduce a fraction to lowest terms.
def reduce(num, den):
    # If the numerator is 0 then the reduced fraction is 0/1
    if num == 0:
        return 0, 1
    # Compute the greatest common divisor of the numerator and denominator
    g = gcd(num, den)

    # Divide both the numerator and denominator by the gcd and return the result
    return num // g, den // g


# Read the fraction from the user and display the reduced fraction
def main():

    num = int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))

    # Compute the reduced fraction
    (n, d) = reduce(num, den)

    print("%d/%d can be reduced to %d/%d. " % (num, den, n, d))


main()
