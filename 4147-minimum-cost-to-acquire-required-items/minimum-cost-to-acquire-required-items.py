class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth>=cost1+cost2:
            return cost1*need1+cost2*need2
        
        if need1>=need2:
            return costBoth*need2+min(cost1, costBoth)*(need1-need2)
        return costBoth*need1+min(cost2, costBoth)*(need2-need1)