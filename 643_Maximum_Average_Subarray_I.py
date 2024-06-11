class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currsum=maxsum=sum(nums[:k])
        
        for i in range(k,len(nums)):
            currsum+=nums[i]-nums[i-k]
            
            maxsum=max(maxsum,currsum)
            
        return maxsum/k
