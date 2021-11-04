class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        
        res = 0
        x_to_y = collections.defaultdict(list)
        y_to_x = dict()
        
        for i, j in points :
            x_to_y[i].append(j)
        
        for x, values in x_to_y.items() :
            n = len(values)
            for i in range(n-1) :
                for j in range(i+1, n) :
                    y1, y2 = values[i], values[j]
                    if (y1, y2) in y_to_x :
                        area = (x - y_to_x[y1, y2]) * (y2 - y1)
                        res = min(res, area) if res else area
                    y_to_x[y1, y2] = x
        
        return res
