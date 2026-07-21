class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=0
        maxProfit=0
        for i in  range(len(prices)):
            if prices[left] > prices[left+1]:
                left=left+1
                right=max(right,left)
            
            

        