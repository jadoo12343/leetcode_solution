class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=[]
        for i in range(len(accounts)):
            imon=0
            for j in range(len(accounts[i])):
                imon+=accounts[i][j]
            wealth.append(imon)
        return max(wealth)

        