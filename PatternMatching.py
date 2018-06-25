# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i) 
    return positions

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(' '.join([str(i) for i in PatternMatching(lines[0],lines[1])]))
