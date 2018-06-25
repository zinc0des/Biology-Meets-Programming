# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = [] # output variable
    # your code here
    Comp = ''
    Comp = reverse(Pattern)
    for c in Comp:
        revComp += complement(c)
        revComp = ''.join(revComp)
    return revComp


# Copy your reverse function from the previous step here.
def reverse(text):
    tip = ''
    for i  in range(1,len(text) + 1):
        tip = tip + text[len(text) - i]
    return tip

# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    # your code here
    if Nucleotide == "A":
            comp = "T"
    if Nucleotide == "C":
            comp = "G"
    if Nucleotide == "T":
            comp = "A"
    if Nucleotide == "G":
            comp = "C"
    return comp
    



### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(ReverseComplement(sys.stdin.read().strip()))
