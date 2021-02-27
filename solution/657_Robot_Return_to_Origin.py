class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
  
    # why is it slower?
#     def judgeCircle(self, moves: str) -> bool:
#         position = [0, 0]
        
#         for i in moves :
#             if i == 'L' : position[0] -= 1
#             elif i == 'R' : position[0] += 1
#             elif i == 'D' : position[1] -= 1
#             else : position[1] += 1
        
#         return position == [0, 0]
