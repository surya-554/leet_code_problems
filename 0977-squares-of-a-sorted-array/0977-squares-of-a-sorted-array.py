class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = []
        for i in nums:
            digit = i * i
            square.append(digit)

        return sorted(square)
        