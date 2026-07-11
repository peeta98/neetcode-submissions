class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matrix = []
        hashmap = {}

        for i in range (0, len(strs)):
            # Map has to be key = sorted str; value = array of all anagram strings
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in hashmap:
                continue
            
            hashmap[sorted_str] = [strs[i]]

            if i == len(strs):
                break

            for j in range (i+1, len(strs)):
                second_sorted_str = "".join(sorted(strs[j]))
                if sorted_str == second_sorted_str:
                    hashmap[sorted_str].append(strs[j])

        for value in hashmap.values():
            matrix.append(value)

        return matrix