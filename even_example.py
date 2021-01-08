# this program lists the even numbers in a range from 2 to
# user entered number

def even_numbers(maximum):
    return_string = ""
    for x in range(0,maximum+1,2):
        return_string += str(x) + " "
    return return_string.strip()

number = int(input("Please enter a number: "))
print(even_numbers(number))
