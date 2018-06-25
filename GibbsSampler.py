# first, import the random package
import random

# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def GibbsSampler(Dna, k, t, N):
    BestMotifs = '' # output variable
    # your code here
    Motifs = RandomMotifs(Dna, k, t)
    BestMotifs = Motifs
    for j in range(N):
        i = random.randint(0, t-1)
        MotifsWithoutMotif_i = Motifs[:i] + Motifs[i+1:] 
        ProfileWithoutMotif_i = ProfileWithPseudocounts(MotifsWithoutMotif_i)
        #Profile_MotifList = ProfileWithPseudocounts(Motifs) - WeightedDie(Pr(ProfileWithPseudocounts(Motifs), i))
        Motifs[i] = ProfileGeneratedString(Dna[i], ProfileWithoutMotif_i, k)
        if Score(Motifs) < Score(BestMotifs):
             BestMotifs = Motifs
    return BestMotifs

# place all subroutines needed for GibbsSampler below this line
def ProfileGeneratedString(Text, profile, k):
    # your code here
    n = len(Text)
    probabilities = {} 
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)
def Normalize(Probabilities):
    # your code here
    #ProbabilitySums = {}
    psum = sum(Probabilities.values())
    for kmer in Probabilities:
        Probabilities[kmer] = Probabilities[kmer] / psum
    return Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    output = ''
    # your code here
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
def RandomMotifs(Dna, k, t):
    # place your code here.
    t = len(Dna[0])
    random_kmer = []
    for i in range(len(Dna)):
        p = random.randint(0, t-k)
        random_kmer.append(Dna[i][p:p+k])
    return random_kmer
def Motifs(Profile, Dna):
    # insert your code here
    t = len(Dna)
    k = len(Profile['A'])
    Motifs = []
    for i in range(t):
        #print(Dna[i])
        Motifs.append(ProfileMostProbablePattern(Dna[i], k, Profile))
    return Motifs
# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
def Pr(Pattern, Profile):
    p = 1
    for i in range(len(Pattern)):
        p = p * Profile[Pattern[i]][i]
    return p
def ProfileMostProbablePattern(Text, k, Profile):
    ProbablePattern = Text[0:k]
    Pattern = ""
    max_p = 0
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        p = Pr(Pattern, Profile)
        if p > max_p:
            max_p = p 
            ProbablePattern = Pattern  
    return ProbablePattern
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
def Score(Motifs):
    count = 0
    k = len(Motifs[0])
    t = len(Motifs)
    ConsensusMotif = Consensus(Motifs)
    for i in range(t):
        for j in range(k):
            if Motifs[i][j] != ConsensusMotif[j]:
                count += 1
    return count
def Consensus(Motifs):
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
def RepeatedGibbsSampler(Dna, k, t, N):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(100):
        Motifs = GibbsSampler(Dna, k, t, N)
        CurrScore = Score(Motifs)
        if CurrScore < BestScore:
            BestScore = CurrScore
            BestMotifs = Motifs
    return BestMotifs
import sys
lines = sys.stdin.read().splitlines()
k,t,N = lines[0].split()
k = int(k)
t = int(t)
N = int(N)
print('\n'.join(RepeatedGibbsSampler(lines[1:],k,t,N)))
