class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Initialize variables
        i = 0
        n = len(s)
        sign = 1
        result = 0
        
        # Define 32-bit signed integer boundaries
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Step 2: Discard leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
            
        # Step 3: Check for sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
            
        # Step 4: Convert digits and handle overflow
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check overflow before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
                
            result = result * 10 + digit
            i += 1
            
        return sign * result