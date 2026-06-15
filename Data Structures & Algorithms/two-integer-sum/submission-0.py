class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if ((nums[i]+nums[j]==target) & (i!=j)):
                    if (i < j):
                        twosum.append(i)
                        twosum.append(j)    
                    else:
                        twosum.append(j)
                        twosum.append(i)
                    return twosum