class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def dfs(letters: str, path: str) :
            res.add(path)
            for i, x in enumerate(letters) :
                dfs(letters[:i] + letters[i+1:], path + x)
        
        dfs(tiles, '')
        return len(res) - 1
