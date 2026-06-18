class Solution:
    def getConcatenation(self, nums):
        ans=[]
        for i in range(len(nums)*2):
            if i>=len(nums):
                ans.append(nums[i-len(nums)])
                
            else:
                ans.append(nums[i])
              
       
        return ans

        
