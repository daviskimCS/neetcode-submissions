class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Initial thoughts (O(nlogn)): 
    # Build a hashmap/dict of the input where key is the value in nums, and value is the noc within nums
    # Sort the hm/dict and use k to return to the keys for highest k values

        # Hashmap/dict to track the value and the number of occurences 
        count = {}
        # List of empty lists (number of empty lists will dependent on input size)
        # this is because the max number of occurences of an element will be bounded by the input size
        freq = [[] for i in range(len(nums) + 1)]

        # Populate hashmap with the key values (num, counts)
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Using the key values from the hashmap using .items(), for index 1 of freq, that means that
        # value occurred once in the input
        for nums, count in count.items():
            freq[count].append(nums)

        # Create empty list to return results
        result = []

        # Iterate through freq list going backwards, as to hit the highest frequencies first
        for i in range(len(freq) - 1, 0, -1):
            # For each num in the freq at the index, append, stopping as soon as we hit k amount
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result