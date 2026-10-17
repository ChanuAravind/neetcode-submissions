from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Dictionary to keep track of frequency of characters in t
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Number of unique characters in t that currently have their frequency 
        # requirements met in the current window
        formed = 0
        
        # Dictionary which keeps track of all the unique characters in the current window
        window_counts = {}
        
        # Tuple of (window length, left, right)
        ans = float("inf"), None, None
        
        l, r = 0, 0
        
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
                
            # Try and contract the window till the point where it ceases to be 'valid'
            while l <= r and formed == required:
                char = s[l]
                
                # Save the smallest window until now
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                l += 1    
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
