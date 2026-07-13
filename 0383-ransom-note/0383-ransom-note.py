class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       # st1 = Counter(ransomNote)
        #st2 = Counter(magazine)

      #  if st1 & st2 == st1:
       #     return True
        #return False
    
        char_counts = {}
        for char in magazine:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        # Step 2: Verify if the magazine has enough characters for the ransom note
        for char in ransomNote:
            # If the character is missing or we ran out of it
            if char not in char_counts or char_counts[char] == 0:
                return False
            char_counts[char] -= 1
            
        return True