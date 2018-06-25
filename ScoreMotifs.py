# Copy your Consensus(Motifs) function here.
def Consensus(Motifs):
    # insert your code here
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACTG":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus
            
# Copy your Count(Motifs) function here.
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
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    # Insert code here
    k = len(Motifs[0])
    t = len(Motifs)
    count = Count(Motifs)
    score = 0
    consensus = Consensus(Motifs)
  
        #unmatchedSymbolCount = ""
    for i in range(t):
        for j in range(k):
            if Motifs[i][j] != consensus[j]:
                #unmatchedSymbolCount = count[symbol][j]
                score += 1
    return score;
            

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(Score(sys.stdin.read().splitlines()))
