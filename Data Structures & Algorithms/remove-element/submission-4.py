class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        last=len(nums)-1
        for i in range(len(nums)):
            if nums[i]==val and i<last:
                while nums[last]==val and last:
                    last-=1
                    
                nums[i],nums[last]=nums[last],nums[i]
                last-=1
                
            # print(nums)
        # print(nums)
        # print(count)
        for i in nums:
            if i!=val:
                count+=1

        return count
    