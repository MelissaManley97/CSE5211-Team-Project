import sys
import cProfile
import io
import pstats
import time

# Knuth Morris Pratt pattern matching
# @param  pattern   The pattern to find within the text
# @param  text      The block of text
# If the pattern is found in the text, this function prints the start
# and end indices of where in text the pattern is located.
def KMPSearch(pattern, text):
	# First initialize the "local state"
	M = len(pattern)
	N = len(text)
	j = 0  # pattern indexer
	i = 0  # text indexer

	# Calculate the strict border for each index in the pattern
	strict_border = [0]*M

	compute_strict_border(pattern, strict_border)

	# Keep trying to find the pattern while the text index is legal
	while i < N:
		# Scan left to right, checking off each match by incrementing
		# the indices
		if pattern[j] == text[i]:
			i += 1
			j += 1

		# If pattern found, return the start/end indices of where
		# in the text the pattern is located
		if j == M:
			return (i - j), (i-1)

		# If there is a mismatch after j matches
		elif text[i] != pattern[j] and i < N:
			# Knuth-Morris-Pratt Shift
			if j == 0:
				i += 1
			else:
				j = strict_border[j - 1]
	return -1,-1


# Computes the strict border for a given pattern
# @param pattern   The text pattern
# @return  List containing all the strict border lengths of the pattern
def compute_strict_border(pattern, strict_border):
	# To keep track of the length of the longest prefix suffix
	longest_prefix_suffix_len = 0

	# First border entry should always be 0
	strict_border[0] = 0

	for i in range(1, len(pattern)):
		# There is still a matching prefix/suffix
		if pattern[i] == pattern[longest_prefix_suffix_len]:
			longest_prefix_suffix_len += 1
			# Compute the border as necessary
			strict_border[i] = longest_prefix_suffix_len
			# Increment to prepare to check the next index for a match
			i += 1
		else:  # Not a prefix/suffix match
			# If there is currently a border, reset the length, since
			# we have reached the end of the current border.
			if longest_prefix_suffix_len != 0:
				longest_prefix_suffix_len = strict_border[longest_prefix_suffix_len - 1]
			else:
				strict_border[i] = 0
				i += 1
                

def main():
    file = open(sys.argv[1], "r")
    text_str = file.readline()
    pattern_str = file.readline()

    pr = cProfile.Profile()
    pr.enable()
    t = time.clock()
    pattern_location = KMPSearch(pattern_str, text_str) 
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
