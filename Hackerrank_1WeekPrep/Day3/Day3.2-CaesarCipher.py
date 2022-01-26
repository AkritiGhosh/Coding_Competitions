# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

#!/bin/python3

# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k - shift/rotate key


def caesarCipher(s, k):
    # Write your code here
    ans = ""
    for i in range(len(s)):
        if s[i].isalpha():
            n = ord(s[i]) + (k%26)
            if((s[i].isupper() and n > 90) or (s[i].islower() and n > 122)):
                n -= 26
            ans += chr(n)
        else:
            ans += s[i]
    return ans

s = input()
k = int(input().strip())
result = caesarCipher(s, k)
print(result)