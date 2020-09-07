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

interesting_nums = {}

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

#the smallest set of consecutive numbers whose product is greater than or equal to 1e8:
#(x-1)^2 + x^2 > 1e8.  
#simplify
#2x^2 - 2x + (-10^8 - 1) > 0

#quadratic formula
a = 2
b = -2
c = -1e8 - 1

upper = (-b + (b**2-4*a*c)**0.5) / (2*a)

if upper != int(upper):
    upper = int(upper) + 1


for n in range(2,upper+1):
    ans = n**2
    for m in range(n-1,0,-1):
        ans += m**2
        # print(f'n: {n}, m: {m}, ans: {ans}')
        if ans > 1e8 or ans < 11:
            break
        if not ans in interesting_nums:
            if isPalindrome(ans):
                interesting_nums[ans] = ''
                print(f'interesting: {ans}')

            
interesting_nums = np.fromiter(interesting_nums.keys(), dtype=float)

print(interesting_nums.sum())