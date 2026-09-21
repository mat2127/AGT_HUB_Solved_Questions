class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        p=0
        
        for s in range(len(nums)):
            if nums[s]!=val:
                nums[p],nums[s]=nums[s],nums[p]
                p+=1
                

        return p
        
        
        