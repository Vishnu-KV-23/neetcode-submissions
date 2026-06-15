class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem={}
        for i,num in enumerate(nums):
            if target-num not in rem:
                rem[num]=i

            else:
                return [rem[target-num],i]        