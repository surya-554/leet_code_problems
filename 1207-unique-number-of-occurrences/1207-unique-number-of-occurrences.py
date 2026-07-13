class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1

        seen = set()
        for value in count.values():
            if value in seen:
                return False

            seen.add(value)

        return True

        
        