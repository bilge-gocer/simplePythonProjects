# Center a string of characters within a certain width.

WIDTH = 80


# Create new string that will be centered within a given width when it is printed.
# @param s the string that will be centered
# @param width the width in which the string will be centered
# @return a new copy of s that contains the leading spaces needed so that
# @param s will appear centered when is printed


def center(s, width):
    # If the string is too long to center, then the original string is returned
    if width < len(s):
        return s

    # Compute the number of spaces needed and generate the result
    spaces = (width - len(s)) // 2
    result = " " * spaces + s

    return result


# Demonstrate the center function
def main():
    print(center("A Famous Story", WIDTH))
    print(center("by:", WIDTH))
    print(center("Someone Famous", WIDTH))
    print()
    print("Once upon a time...")


# Call the main function
main()
