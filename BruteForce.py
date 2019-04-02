import sys
import cProfile
import io
import pstats
import time


# Brute force pattern matching (left to right scan)
# @param  text      The block of text
# @param  pattern   The pattern to find within the text
# @return Pair of the start and end indices of where in text the pattern is located
# If the text is not found in the pattern, this function returns (-1,-1)
def brute_force(text, pattern):
    i = 0
    n = len(text)
    m = len(pattern)
    j = 0
    while i <= n-m:
        # Left-right scan
        while (j < m) and (pattern[j] == text[i+j]):
            j += 1
        # If pattern found, return the start/end indices of where
        # in the text the pattern is located
        if j == m:
            return i, (i+j-1)
        # Shift pattern one place in text to try again
        i += 1
        j = 0
    #  Pattern not found
    return -1, -1


def main():
    # For each test file in this directory: run it and print results
    # Read input file to get string and pattern
    file = open(sys.argv[1], "r")
    text_str = file.readline()
    pattern_str = file.readline()

    # Profile the three algorithms
    # Start profiler
    pr = cProfile.Profile()
    pr.enable()
    t = time.clock() # Start clock (more accurate time than profiler)
    pattern_location = brute_force(text_str, pattern_str)
    print(time.clock()-t) # Stop clock
    # Stop profiling
    pr.disable()
    s = io.StringIO()
    sortBy = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortBy)
    ps.print_stats()
    print(s.getvalue())

if __name__ == "__main__":
    main()
