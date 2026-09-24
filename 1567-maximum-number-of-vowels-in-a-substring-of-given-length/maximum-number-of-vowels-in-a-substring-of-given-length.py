class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vow=['a', 'e', 'i', 'o','u']
        counter=0
        left=0
        for i in range(k):
            
            if s[i] in vow:
                counter+=1
        max_counter=counter    
        for right in range(k,len(s)):
            if s[left] in vow:
                counter -= 1

            
            if s[right] in vow:
                counter += 1

            left += 1
            max_counter=max(counter,max_counter)
             
             
             
             
        return max_counter
        