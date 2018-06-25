# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
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
# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
A = [float(c) for c in lines[0].split()]
C = [float(c) for c in lines[1].split()]
G = [float(c) for c in lines[2].split()]
T = [float(c) for c in lines[3].split()]
Profile = {'A':A,'C':C,'G':G,'T':T}
Dna = lines[4:]
print('\n'.join(Motifs(Profile,Dna)))
