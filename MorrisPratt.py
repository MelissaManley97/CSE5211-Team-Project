import sys
import cProfile
import io
import pstats
import time


# Morris Pratt Strings will contain
# the actual given string and its computed borders
class MP_String:
    def __init__(self, text):
        self.string = text
        self.border = compute_border(text)


# Computes the borders for a given pattern
# @param pattern   The text pattern
# @return  List containing all the border lengths of the pattern
def compute_border(pattern):
    # Initialize borders array
    border = [0 for i in range(len(pattern)+1)]
    # First entry should always be -1
    border[0] = -1
    b = -1

    # For each non-empty prefix
    for j in range(1, len(pattern)+1):
        # Find the length of the longest border of prefix pattern[0..(j-1)].
        # Reduce the border until a match is found or no border exists
        while b >= 0 and not (pattern[b] == pattern[j - 1]):
            b = border[b]
        # Extend the border by one character when next characters match
        b += 1
        border[j] = b
    return border


# Morris Pratt pattern matching
# @param  text      The block of text
# @param  pattern   The pattern to find within the text
# @return Pair of the start and end indices of where in text the pattern is located
# If the text is not found in the pattern, this function returns (-1,-1)
def morris_pratt(text, pattern):
    # Same as brute force except for how shifts are made when there is a mismatch
    i = 0
    n = len(text)
    m = len(pattern.string)
    j = 0
    # Keep trying to find the pattern while the text index is legal
    while i <= n - m:
        # Left-right scan
        while (j < m) and (pattern.string[j] == text[i + j]):
            j += 1
        # If pattern found, return the start/end indices of where
        # in the text the pattern is located
        if j == m:
            return i, (i+j-1)
        # Morris-Pratt Shift
        i = i + j - pattern.border[j]
        if 0 < pattern.border[j]:
            j = pattern.border[j]
        else:
            j = 0
    #  Pattern not found
    return -1, -1


def main():
    # For each test file in this directory: run it and print results
    # Read input file to get string and pattern
    file = open(sys.argv[1], "r")
    text_str = file.readline()
    pattern_str = file.readline()
    pattern = MP_String(pattern_str)

   # Profile the three algorithms
    # Start profiler
    pr = cProfile.Profile()
    pr.enable()
    t = time.clock() # Start clock (more accurate time than profiler)
    # Run algorithm
    pattern_location = morris_pratt(text_str, pattern)
    print(time.clock()-t) # Stop clock
    # Stop profiling
    pr.disable()
    s = io.StringIO()
    sortBy = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortBy)
    ps.print_stats()
    print(s.getvalue())
    file.close()

if __name__ == "__main__":
    main()
