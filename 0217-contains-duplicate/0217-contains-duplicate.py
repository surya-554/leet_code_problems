class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        yog = set()
        for a in nums:
            if a in yog:
                return True
            yog.add(a)
        return False

        