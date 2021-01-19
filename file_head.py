#
# -- Display the head(first 10 lines) of a file whose name is provided as a command line parameter.
#


import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print("You must provide the file name as a command line parameter.")
    quit()

try:
    inf = open(sys.argv[1], "r")

    line = inf.readline()

    count = 0
    while count < NUM_LINES and line != "":
        line = line.rstrip()
        count = count + 1

        print(line)

        line = inf.readline()

    inf.close()

except IOError:
    print("There is a problem occurred. ")
