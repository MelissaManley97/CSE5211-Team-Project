import random
import string

def main():
    # Open the file and set to overwrite data
    f = open("stressTest.txt", "w")
    # Set number of docks and instructions
    numChars = 3000000
    wholeString = ""
    pattern = "oooooooooooooooooooooh"

    # Loop through the number of instructions
    for i in range(numChars):
        # Choose any lowercase ascii character
        currentChar = 'o'
        wholeString += currentChar
        # Write to file, all on one line
        f.write(currentChar)
    # Add ending character so pattern can be found
    f.write('h')
    
    # Make the desired pattern at the end of the string and
    # add pattern to second line
    f.write("\n%s" % (pattern))

if __name__ == "__main__":
    main()


