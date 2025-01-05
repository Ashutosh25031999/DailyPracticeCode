class Solution:
    def canCompleteCircuit(self, gas, cost):
        sum_cost = sum(cost)
        sum_gas = sum(gas)
        if sum_cost > sum_gas:
            return -1

        current_gas = 0
        starting_index = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                starting_index = i + 1
        return starting_index


solution = Solution()

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

starting_index = solution.canCompleteCircuit(gas, cost)
print(starting_index) 
