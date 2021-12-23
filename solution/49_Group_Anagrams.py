class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for word in strs :
            groups[str(sorted(word))].append(word)
        return groups.values()
