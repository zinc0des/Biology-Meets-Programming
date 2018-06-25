def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    k = len(Motifs[0])
    for symbol in "ACTG":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count  
# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    profile = Count(Motifs)
    for i in profile:
        for j in range(len(profile[i])):
            profile[i][j] *= float(1/t)
    return profile

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(Profile(sys.stdin.read().splitlines()))
