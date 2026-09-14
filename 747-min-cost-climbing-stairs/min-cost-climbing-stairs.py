class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={}
        n=len(cost)
        def less_cost(i):
            if i<=1:
                return cost[i]
            if i in cache:
                return cache[i]

            cache[i]=cost[i]+min(less_cost(i-1), less_cost(i-2))
            return cache[i]
        return min(less_cost(n-1), less_cost(n-2))

 
        
        # def min_cost(i):
        #     n=len(cost)
        #     if i<=1:
        #         return cost[i]
        #     return cost[i]+min(min_cost(i-1), min_cost(i-2))
        # return min(min_cost(n-1), min_cost(n-2))