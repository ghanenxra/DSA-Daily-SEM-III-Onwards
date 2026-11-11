class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        min_need=min(need1, need2)
        total=min_need*min(costBoth, cost1+cost2)

        case1=need1-min_need
        total+=case1*min(costBoth, cost1)

        case2=need2-min_need
        total+=case2*min(costBoth, cost2)

        return total










        # min_need=min(need1, need2)
        # if need1==need2==0:
        #     return 0
        # temp=(cost1*need1, cost2*need2, costBoth*min(need1, need2))
        # return (cost1*need1+cost2*need2+costBoth*min(need1, need2))-max(cost1*need1, cost2*need2, costBoth*min(need1, need2))




        # elif need1>need2:
        #     return min(cost1*need2+cost2*need2,costBoth*need2)+(need1-need2)*min(costBoth,cost1+cost2)
        # elif need2>need1:
        #     return min(cost1*need1+cost2*need1,costBoth*need1)+(need2-need1)*min(costBoth,cost1+cost2)
        # return min(cost1*need1+cost2*need2, costBoth*max(need1,need2))
