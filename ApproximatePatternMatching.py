# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    # your code here
    for i in range(len(Text)):
        try:
            subtext = Text[i:(len(Pattern)+i)]
        except(IndexError):
            continue
        else:
            if len(Pattern) == len(subtext):
                if HammingDistance(Pattern, subtext) <= d:
                    pos = i
                    positions.append(pos)
    return positions


# Insert your Hamming distance function on the following line.
def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
            if p[i] is not q[i]:
                count = count + 1
    return count

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(' '.join([str(i) for i in ApproximatePatternMatching(lines[0],lines[1],int(lines[2]))]))
