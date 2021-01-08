def is_palindrome(input_string):
    #We wil create two strings, to compare them

    new_string = ""
    reverse_string = ""

    #Traverse through each letter of the input string

    for string in input_string.lower():
        # add any non-blank letters to the end of one string, and to the front of the other string

        if string.replace(" ",""):
            new_string = string + new_string
            reverse_string = string + reverse_string
    # compare the strings

    if new_string[::-1] == reverse_string:
        return True
    return False

word = input("Please enter a word: ")
print(is_palindrome(word))
