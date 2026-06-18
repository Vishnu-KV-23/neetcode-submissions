class Solution:
    def getConcatenation(self, nums):
        ans=[0]*(len(nums)*2)
        for i in range(len(ans)):
            if i>=len(nums):
                ans[i]=nums[i-len(nums)]
                # print(f"ans[{i}]={ans[i]}   nums[{i}]={nums[i]}")
            else:
                ans[i]=nums[i]
                # print(f"ans[{i}]={ans[i]}   nums[{i}]={nums[i]}")

        # print(ans)
        return ans
        
        
# Solution().getConcatenation([1,2,3])