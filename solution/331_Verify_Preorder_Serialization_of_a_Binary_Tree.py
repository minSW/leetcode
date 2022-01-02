import re

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        while preorder != "#" :
            tmp = re.sub('[0-9]+,#,#', '#', preorder)
            if tmp == preorder : 
                return False
            preorder = tmp
        return True
