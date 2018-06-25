# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
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
print(HammingDistance(lines[0],lines[1]))
