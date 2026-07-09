class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        i = 0
        j = n
        while i < n:
            result.append(nums[i])
            result.append(nums[j])

            i = i + 1
            j = j + 1

        return result
        