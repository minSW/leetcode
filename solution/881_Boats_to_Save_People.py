class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats, n = 0, len(people)
        lightest = n-1
        people.sort(reverse=True)
        
        for i in range(n) :
            if i > lightest : break
            if people[i] + people[lightest] <= limit : lightest -= 1
            boats += 1
        
        return boats
