class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p=0
        for s in range(len(nums)):
            if nums[p]<nums[s]:
                p+=1
                nums[p],nums[s]=nums[s],nums[p]
        return p+1
        
            

       
        