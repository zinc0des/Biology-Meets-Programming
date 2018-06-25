# Input:  A String Genome
# Output: Skew(Genome)
def Skew(Genome):
    skew = {} #initializing the dictionary
    # your code here
    start = ' ';
    Genome = start + Genome;   
    for i in range(len(Genome)):  
            if Genome[i] == ' ': 
                skew[i] = 0
            elif Genome[i] == 'G':
                skew[i] = skew[i-1]+1
            elif Genome[i] == 'C':
                skew[i] = skew[i-1]-1
            else:
                skew[i] = skew[i-1]
    return skew


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
skew = Skew(sys.stdin.read().strip())
print(' '.join([str(skew[i]) for i in sorted(skew.keys())]))
