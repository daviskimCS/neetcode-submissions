class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create dictionary to store key value pairs
        # keys will include all different integers found in nums
        # value will be number of times it appears in nums
        # 1. initialize dict
        # 2. loop through the array, appending each integer to dict
        # 3. as soon as we try appending an already present integer
        #    we return false
        # 4. if we make it through nums w.out doing so, return true

        dict = {}
        
        for num in nums:
            if dict.get(num) == None:
                dict.update({num:1})
            else:
                return True
        
        return False
        