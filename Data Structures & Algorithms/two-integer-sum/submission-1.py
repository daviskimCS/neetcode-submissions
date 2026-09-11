class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store the key and index of the value to easily retrieve if is solution
        numsDict = {} 
        
        # Enumerate list to make into 2d array with index and value
        for i, value in enumerate(nums):
            # For current index compute the difference between the target value and current index's value. If the complement aka the difference exists within the hash map that stores the past "seen" (iterated over previously) values, then that is the solution indices. 
            difference = target - value
            if difference in numsDict:
                return[numsDict[difference], i]

            # If the index is not the second solution index, add to the hashmap of seen values
            numsDict[value] = i

# Edge cases where we go over two of the same value? Storing the indices? 