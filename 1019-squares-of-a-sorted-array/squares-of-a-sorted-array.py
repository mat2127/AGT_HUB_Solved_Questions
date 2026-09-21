class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left=0
        right=len(nums)-1
        arr=[0]*len(nums)
        p=len(nums)-1
        while left<=right:
            if nums[left]*nums[left]<nums[right]*nums[right]:
                arr[p]=nums[right]*nums[right]
                right-=1
            else:
                arr[p]=nums[left]*nums[left]
                left+=1
            p-=1
        return arr


        