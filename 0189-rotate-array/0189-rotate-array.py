class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
    
        """
        num = len(nums)
        ans = [0] * num
        for i in range(num):
            new_index = (i+k) % num
            ans[new_index] = nums[i]
        for i in range(num):
            nums[i] = ans[i]
        


        