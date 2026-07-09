class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = " "
        for digit in digits:
            num = num + str(digit)

        num = int(num) + 1

        arr = []
        for digit in str(num):
            arr.append(int(digit))
        return arr


        