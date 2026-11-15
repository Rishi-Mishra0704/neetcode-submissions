class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}                               
        for word in strs:
            counts = [0] * 26                      
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            signature = tuple(counts)   

            if signature not in groups:
                groups[signature] = []
            groups[signature].append(word)
        return list(groups.values())