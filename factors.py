# Count factorial numbers in a given range

def factorial(num):
    result = 1
    for x in range(1, num + 1):
        result = result * x
    return result


number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
for n in range(number1, number2):
    print(n, factorial(n))
