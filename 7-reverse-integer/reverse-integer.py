class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer limits
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        
        # Track the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits using string manipulation
        reversed_x = int(str(x)[::-1]) * sign
        
        # Check if the result falls outside the 32-bit integer range
        if reversed_x < MIN_INT or reversed_x > MAX_INT:
            return 0
            
        return reversed_x