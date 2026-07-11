class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        new = 0
        
        # Count vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                new += 1
        
        ans = new
        
        # Slide the window across the rest of the string
        for i in range(k, len(s)):
            # Remove the element going out of the window
            if s[i - k] in vowels:
                new -= 1
            # Add the new element entering the window
            if s[i] in vowels:
                new += 1
            # Track the maximum count seen so far
            ans = max(ans, new)
            
        return ans