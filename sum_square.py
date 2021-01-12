# it returns the sum of all the squares of numbers between 0 and x(not included).

def square(n):
    return n * n


def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum


number = int(input("Please enter a number: "))
print(number, " of sum square is: ", sum_squares(number))
