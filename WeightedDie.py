# first, import the random package
import random
# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    output = ''
    p = random.uniform(0,1)
    s = 0.0
    WeightedProb = {}
    for kmer in Probabilities:
        WeightedProb[kmer] = (s, s + Probabilities[kmer])
        s = s + Probabilities[kmer]
    for kmer in WeightedProb:
        if p >= WeightedProb[kmer][0] and p <= WeightedProb[kmer][1]:
            output = kmer
    return output


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys,inspect
dic = {}
lines = sys.stdin.read().splitlines()
it = int(lines[0])
for line in lines[1:]:
    p,kmer = line.split()
    dic[kmer] = float(p)
for i in range(it):
    print(WeightedDie(dic))
