class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for str in strs:
            encoded_string += f"{len(str)}#{str}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j]) # e.g., "5#Hello5#World": 1st) 5# = 5 | Length = 5
            word = s[j + 1 : j + 1 + length] # 1st) "H" -> "o"
            strs.append(word) # 1st) strs = ["Hello"]
            i = j + 1 + length # 1st) i = 1 + 1 + 5 = 7 -> "5"
        return strs