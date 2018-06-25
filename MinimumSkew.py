#Write a function MinSkew taking a DNA string Genome as input and returning all integers i minimizing Skew[i] for Genome. Then add this function to Replication.py. (Hint: make sure to call Skew(Genome) as a subroutine, and keep in mind that Python has a built-in min function in addition to max.)
# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    skew = Skew(Genome)
    n = min(skew.values())
    for i in skew:
        if skew[i] == n:
             pos = i  
             positions.append(pos)
    return positions

# Input:  A String Genome
# Output: Skew(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def Skew(Genome):
    skew = {} # output variable
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
print(' '.join([str(i) for i in MinimumSkew(sys.stdin.read().strip())]))
