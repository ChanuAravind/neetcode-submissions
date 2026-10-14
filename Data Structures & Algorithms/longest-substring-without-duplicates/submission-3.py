# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_len=0
#         i,j=0,1

#         while j<=len(s):
#             # if len(set(s[i:j])) == len(s[i:j]):
#             if len(set(s[i:j])) == len(s[i:j]):
#                 if max_len < j-i:
#                     max_len = j-i
#                 j+=1
#             else:
#                 i+=1
            
#         return max_len




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i = 0
        char_set = set()

        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1

            char_set.add(s[j])
            max_len = max(max_len, j - i + 1)

        return max_len
