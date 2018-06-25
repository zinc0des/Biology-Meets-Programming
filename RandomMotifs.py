# import Python's 'random' module here
import random
# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t):
    # place your code here.
    t = len(Dna[0])
    random_kmer = []
    for i in range(len(Dna)):
        p = random.randint(0, t-k)
        random_kmer.append(Dna[i][p:p+k])
    return random_kmer

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
k,t = lines[0].split()
k = int(k)
t = int(t)
print('\n'.join(RandomMotifs(lines[1:],k,t)))
