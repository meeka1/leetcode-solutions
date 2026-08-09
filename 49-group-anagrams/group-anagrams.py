from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        results = []

        for s in strs:
            sorted_letters = tuple(sorted(s))
            anagrams[sorted_letters].append(s)

        return list(anagrams.values())
