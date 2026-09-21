class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p=0
        for s in range(len(nums)):
            if nums[s]!=0:
                nums[p],nums[s]=nums[s],nums[p]
                p+=1
        
        