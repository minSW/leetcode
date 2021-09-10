class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101
        for start, end in logs :
            for i in range(start - 1950, end - 1950) :
                population[i] += 1
        return population.index(max(population)) + 1950
