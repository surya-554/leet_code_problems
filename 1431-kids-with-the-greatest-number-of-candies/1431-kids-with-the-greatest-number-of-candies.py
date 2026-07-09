class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        num = []
        maxi = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxi:
                num.append(True)
            else:
                num.append(False)
        return num

        