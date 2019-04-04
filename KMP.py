import sys
import cProfile
import io
import pstats
import time

# Python program for KMP Algorithm 
def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
  
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 
  
    i = 0 # index for txt[] 
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            return i-j
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    return -1

def computeLPSArray(pat, M, lps): 
    len = 0 # length of the previous longest prefix suffix 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            if len != 0: 
                len = lps[len-1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
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
