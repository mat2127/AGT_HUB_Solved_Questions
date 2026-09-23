class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum=0
        for i in range(k):
            window_sum+=nums[i]
        max_sum=window_sum
        left=0
        for right in range(k,len(nums)):
            window_sum+=nums[right]
            window_sum-=nums[left]
            left+=1
            max_sum=max(max_sum,window_sum)
        return max_sum/k

        