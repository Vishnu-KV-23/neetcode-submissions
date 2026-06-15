class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not sorted(nums)==sorted(list(set(nums)))