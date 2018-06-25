# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    # your code here
    for i in range(len(Text)):
        subtext = Text[i:(len(Pattern)+i)]
        if len(Pattern) == len(subtext):
                    if HammingDistance(Pattern, subtext) <= d:
                       count += 1
    return count


# Insert your HammingDistance function on the following line.
def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
            if p[i] is not q[i]:
                count = count + 1
    return count
