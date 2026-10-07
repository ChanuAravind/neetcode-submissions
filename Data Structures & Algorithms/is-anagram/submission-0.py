class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_word_count = dict()
        map_word_count_t = dict()

        for i in range(len(s)):
            if s[i] in map_word_count:
                map_word_count[s[i]] += 1
            else:
                map_word_count[s[i]] = 1

        for i in range(len(t)):
            if t[i] in map_word_count_t:
                map_word_count_t[t[i]] += 1
            else:
                map_word_count_t[t[i]] = 1

        return map_word_count == map_word_count_t