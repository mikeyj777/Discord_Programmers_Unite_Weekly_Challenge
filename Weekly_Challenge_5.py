# *CODING CHALLENGE #5*

# Difficulty: *medium*

# The palindromic number 595 is interesting because it can be written as the sum of consecutive 
#squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

# There are exactly eleven palindromes below one-thousand that can be written as consecutive 
#square sums, and the sum of these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares of positive integers.

# *QUESTION:*
# Find the sum of all the numbers less than 10^8 that are both palindromic and can be
# written as the sum of consecutive squares.


# *MEDIUM OF ANSWER:*
# Post your answer along with the code (github link/link to the code snippet using
# pastebin or some other tool) in <#725633721838993479>. 

# *Good Luck! Have fun!*

import numpy as np

interesting_nums = []
ssqdict = {}

def isPalindrome(n):
    n = str(n)
    fwdchar = 0
    bkwdchar = -1
    while True:
        if fwdchar >= len(n):
            return True
        if n[fwdchar] != n[bkwdchar]:
            return False
        fwdchar += 1
        bkwdchar -= 1

ssqdict[1] = 1

for n in range(11,1e8+1):
    if isPalindrome(n):
        for m in range(1,n-1):
            if not m in ssqdict:
                ssqdict[m] = ssqdict[m-1] + m**2
            if ssqdict[m] == n:
                interesting_nums.append(n)
                print(n)
                break
            if ssqdict[m] > n:
                ans = ssqdict[m]
                breakout = False
                for l in range(1,m-1):
                    ans -= ssqdict[l]
                    if ans == n:
                        interesting_nums.append(n)
                        print(n)
                        breakout = True
                        break
                if breakout:
                    break