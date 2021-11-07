class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces_dict = { piece[0] : piece for piece in pieces }
        return arr == sum([ pieces_dict[a] for a in arr if a in pieces_dict ], [])
