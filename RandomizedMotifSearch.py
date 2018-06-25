# import the random package here
import random
# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
    # insert your code here
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 

# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.
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
def RepeatedRandomizedMotifSearch(Dna, k, t):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(1000):
        Motifs = RandomizedMotifSearch(Dna, k, t)
        CurrScore = Score(Motifs)
        if CurrScore < BestScore:
            BestScore = CurrScore
            BestMotifs = Motifs
    return BestMotifs
import sys
lines = sys.stdin.read().splitlines()
k,t = lines[0].split()
k = int(k)
t = int(t)

print('\n'.join(RepeatedRandomizedMotifSearch(lines[1:],k,t)))
