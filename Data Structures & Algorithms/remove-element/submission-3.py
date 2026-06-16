class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        last=len(nums)-1
        for i in range(len(nums)):
            if nums[i]==val and i<last:
                if i>last:
                    break
                while nums[last]==val and last > i:
                    last-=1
                    
                nums[i],nums[last]=nums[last],nums[i]
                last-=1
                count+=1
        #     print(nums)
        # print(nums)
        # print(count)
        return count
    