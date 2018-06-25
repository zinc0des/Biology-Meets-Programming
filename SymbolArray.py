# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    # type your code here
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array


# Reproduce the PatternCount function on the following line from Replication.py.
def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(SymbolArray(lines[0],lines[1]))
