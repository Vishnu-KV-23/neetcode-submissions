class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1=list(set(nums))
        if len(nums1)!=len(nums):
            return True
        else:
            return False
        