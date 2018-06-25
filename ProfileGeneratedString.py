# first, import the random package
import random
# then, copy Pr, Normalize, and WeightedDie below this line
def Pr(Pattern, Profile):
    p = 1
    for i in range(len(Pattern)):
        p = p * Profile[Pattern[i]][i]
    return p
def Normalize(Probabilities):
    # your code here
    psum = sum(Probabilities.values())
    for kmer in Probabilities:
        Probabilities[kmer] = Probabilities[kmer] / psum
    return Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    p = random.uniform(0,1)
    s = 0.0
    WeightedProb = {}
    for kmer in Probabilities:
        WeightedProb[kmer] = (s, s + Probabilities[kmer])
        s = s + Probabilities[kmer]
    for kmer in WeightedProb:
        if p >= WeightedProb[kmer][0] and p < WeightedProb[kmer][1]:
            output = kmer
    return output
# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    # your code here
    n = len(Text)
    probabilities = {} 
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)
### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
it,Text,profile,k = sys.stdin.read().splitlines()
it = int(it)
profile = eval(profile)
k = int(k)
print('\n'.join([ProfileGeneratedString(Text,profile,k) for i in range(it)]))
