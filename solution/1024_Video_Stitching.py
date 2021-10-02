class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: (x[0], -x[1]))
        seconds = [0] * time
        prev = -1
        
        for start, end in clips :
            if start == prev : continue
            for i in range(start, end) :
                if i >= time : break
                seconds[i] = max(seconds[i], end)
            prev = start
        
        cnt = x = 0
        while x < time :
            x, cnt = seconds[x], cnt + 1
            if not x : return -1
        return cnt
