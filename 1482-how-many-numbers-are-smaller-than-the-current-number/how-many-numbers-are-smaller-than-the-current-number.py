class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        count=[]
        for i in range(len(nums)):
            num=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    num+=1
            count.append(num)
        return count
        


        