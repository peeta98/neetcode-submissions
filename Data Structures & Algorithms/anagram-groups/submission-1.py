class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matrix = []
        hashmap = {}

        for word in strs:
            # Map has to be key = sorted str; value = array of all anagram strings
            sorted_str = "".join(sorted(word))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(word)
            else:
                hashmap[sorted_str] = [word]

        for value in hashmap.values():
            matrix.append(value)

        return matrix