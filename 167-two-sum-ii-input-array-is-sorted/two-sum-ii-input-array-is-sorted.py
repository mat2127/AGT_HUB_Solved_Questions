class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        a=0
        b=len(numbers)-1
        while numbers[a]+numbers[b]!=target:
            if numbers[a]+numbers[b]>target:
                b-=1
            elif numbers[a]+numbers[b]<target:
                a+=1
        return [a+1,b+1]

       
        
        
            
            
        