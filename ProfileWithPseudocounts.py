# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {} # output variable
    # your code here
    profile = CountWithPseudocounts(Motifs)
    for i in profile:
        for j in range(len(profile[i])):
            profile[i][j] *= 1/(t + 4.0)
    return profile

# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
# HINT:   You need to use CountWithPseudocounts as a subroutine of ProfileWithPseudocounts
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    # your code here
    count = {} # initializing the count dictionary
    for symbol in "ACTG":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count                                                                                                                                                                                                                                  



### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(ProfileWithPseudocounts(sys.stdin.read().splitlines()))
