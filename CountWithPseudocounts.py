# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    # insert your code here
    count = {} # initializing the count dictionary
    # your code here
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
print(CountWithPseudocounts(sys.stdin.read().splitlines()))
