class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            s_word = ''.join(sorted(word))
            anagrams[s_word].append(word)
            
        return anagrams.values()