class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Buy=prices[0]
        Profit=0
        for i in range(1,len(prices)):
            if prices[i]<Buy:
                Buy=prices[i]
            else:
                Profit=max(Profit,prices[i]-Buy)
                
        return Profit
        
