class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        

        window = sum(nums[:k])
        new = window 
        for i in range(k, len(nums)):
            window = window - nums[i-k] + nums[i]
            new = max(new,window)

        return new / float(k)
