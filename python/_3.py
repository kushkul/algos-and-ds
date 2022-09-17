class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        i=j=0
        maxlen=0
        while j<len(s):
            if s[j] in char_map.keys():
                i = max(i, char_map[s[j]])
            
            char_map[s[j]] = j+1
            maxlen = max(maxlen, j-i+1)
            j+=1
        
        return maxlen
