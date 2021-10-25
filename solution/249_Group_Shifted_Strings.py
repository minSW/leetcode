class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        diff_dict = collections.defaultdict(list)
        for string in strings :
            key = "".join([ chr((26 + ord(string[i+1]) - ord(string[i])) % 26) for i in range(len(string)-1) ])
            diff_dict[key].append(string)
        return diff_dict.values()
