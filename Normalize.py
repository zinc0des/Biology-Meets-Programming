# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
    # your code here
    #ProbabilitySums = {}
    psum = sum(Probabilities.values())
    for kmer in Probabilities:
        Probabilities[kmer] = Probabilities[kmer] / psum
    return Probabilities

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(Normalize(eval(sys.stdin.read().strip())))
