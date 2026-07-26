class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx=0
        for i in range(len(accounts)):
            mx=max(mx,sum(accounts[i]))
        return mx

        