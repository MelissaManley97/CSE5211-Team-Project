import random
import string

def main():
    # Open the file and set to overwrite data
    f = open("stressTest.txt", "w")
    # Set number of docks and instructions
    numChars = 1000
    wholeString = ""
    pattern = "thisshouldbeattheend"

    # Loop through the number of instructions
    for i in range(numChars):
        # Choose any lowercase ascii character
        currentChar = random.choice(string.ascii_lowercase)
        wholeString = wholeString + currentChar
        # Write to file, all on one line
        f.write(currentChar)
    
    # Make the desired pattern at the end of the string and
    # add pattern to second line
    f.write("%s \n%s" % (pattern, pattern))

if __name__ == "__main__":
    main()


