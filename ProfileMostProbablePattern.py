# Insert your Pr(Text, Profile) function here from Motifs.py.
def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p
# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
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
                
### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
Text = lines[0]
k = int(lines[1])
A = [float(c) for c in lines[2].split()]
C = [float(c) for c in lines[3].split()]
G = [float(c) for c in lines[4].split()]
T = [float(c) for c in lines[5].split()]
Profile = {'A':A, 'C':C, 'G':G, 'T':T}
print(ProfileMostProbablePattern(Text,k,Profile))
