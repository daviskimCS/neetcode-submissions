class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        # defaultdict makes it so that if any element is accessed that is not present in the dictionary it will be created rather than throwing an error. additionally, the new element created will be of the passed in argument type
        result = defaultdict(list)
            
        # for each string, initialize an empty array/list that will keep track of the number of occurrences, where the index represents the type of char
        for string in strings:
            count = [0] * 26

            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1
            
            # redeclaring as a tuple as to be hashable as a key
            key = tuple(count)
            result[key].append(string)

        # redeclaring as a list for expected format
        # outputting all values of dict, which are grouped by the same keys
        return list(result.values())

        # Check if any keys are similar if so, group the values which are the strings
    
    # Initial thought process
        # Edge case for empty input (O(1))

        # For every input string, build a hashmap (dictionary) where each
        # key represents the char and value represents the number of occurrences (O(n))
        # creating a list of the hashmaps

        # For every input string, note the number of keys and check if any strings' hashmap is equal to each 