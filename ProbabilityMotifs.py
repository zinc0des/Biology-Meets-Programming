# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
Text = lines[0]
A = [float(c) for c in lines[1].split()]
C = [float(c) for c in lines[2].split()]
G = [float(c) for c in lines[3].split()]
T = [float(c) for c in lines[4].split()]
Profile = {'A':A, 'C':C, 'G':G, 'T':T}
print(Pr(Text,Profile))
