class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        word_s, word_t = {}, {}
        
        for char_s in s:
            if char_s not in word_s:
                word_s[char_s] = 1
            
            else:
                word_s[char_s] += 1
                
        for char_t in t:
            if char_t not in word_t:
                word_t[char_t] = 1
            
            else:
                word_t[char_t] += 1
    
        for char in s:
        
            if char not in word_t or word_t[char] != word_s[char]:
                return False
            
        return True