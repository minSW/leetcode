class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        index_dict = { a : list() for a in A }
        for i in range(len(B)) :
            index_dict[B[i]].append(i)
        
        return [ index_dict[a].pop() for a in A ]
