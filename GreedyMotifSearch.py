# Copy your Score(Motifs), Count(Motifs), Profile(Motifs), and Consensus(Motifs) functions here.
def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

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
    count = Count(Motifs)

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

def Profile(Motifs):
    profile = {}
    t = len(Motifs)
    k = len(Motifs[0])
    CountMotifs = Count(Motifs)

    for symbol in "ACGT":
        profile[symbol] = []

    for x in CountMotifs:
        for y in CountMotifs[x]:
            z = y/float(t)
            profile[x].append(z)

    return profile

def Count(Motifs):
    count = {}
    k = len(Motifs[0])

    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count
# Then copy your ProfileMostProbablePattern(Text, k, Profile) and Pr(Text, Profile) functions here.
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
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
# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    # type your GreedyMotifSearch code here.
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
               BestMotifs = Motifs
    return BestMotifs
### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
k,t = lines[0].split()
k = int(k)
t = int(t)
print('\n'.join(GreedyMotifSearch(lines[1:],k,t)))
