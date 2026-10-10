class Solution:
    def check_alphanum(self,c:str) -> bool:
        if ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'): 
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        left,right = 0, len(s)-1

        while left<= right:
            if self.check_alphanum(s[left]) and self.check_alphanum(s[right]) and s[left].lower() !=s[right].lower():
                return False
            elif not self.check_alphanum(s[left]):
                left+=1
                continue
            elif not self.check_alphanum(s[right]):
                right-=1
                continue
            left+=1
            right-=1
        return True
            

