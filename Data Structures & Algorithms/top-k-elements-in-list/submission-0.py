class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num]+=1
        buckets = [[] for _ in range(len(nums)+1) ]
        for number, count in freq.items():
            buckets[count].append(number)
        
        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for number in buckets[count]:
                result.append(number)
                if len(result) == k:
                    return result
        return result