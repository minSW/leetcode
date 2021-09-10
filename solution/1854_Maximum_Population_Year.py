class Solution:
    # O(n)
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101
        for start, end in logs :
            population[start-1950] += 1
            population[end-1950] -= 1
        for i in range(1, len(population)) :
            population[i] += population[i-1]
        return population.index(max(population)) + 1950
        
    # O(n^2)
    # def maximumPopulation(self, logs: List[List[int]]) -> int:
    #     population = [0] * 101
    #     for start, end in logs :
    #         for i in range(start - 1950, end - 1950) :
    #             population[i] += 1
    #     return population.index(max(population)) + 1950
