class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #return nums + nums

        empty = []
        for i in nums:
            empty.append(i)
        for i in nums:
            empty.append(i)
        return empty

        