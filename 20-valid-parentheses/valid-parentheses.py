class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                
                temp_pop = stack.pop()

                if temp_pop != dict[ch]:
                    return False

        return len(stack) == 0
                    

            