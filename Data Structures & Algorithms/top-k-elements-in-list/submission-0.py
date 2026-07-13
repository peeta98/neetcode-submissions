class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        k_most_frequent = []

        for num in nums:
            hashmap[num] += 1 # e.g., {1: 3, 2: 1} => [1, 1, 1, 2]

        sorted_nums = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        return [num for num, count in sorted_nums[:k]]
        