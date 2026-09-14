class Solution:
    def encode(self, strs: List[str]) -> str:
        # If passed in empty List, return empty list as encoded
        if not strs:
            return ""
        
        # Create two lists, one to track the sizes of the words to be encoded
        # The second, formatted to be sent over the network
        sizes, result = [], []

        # Using each string in the input list, create a mirror that is of the sizes
        for string in strs:
            sizes.append(len(string))

        # Result will first have the length of the strings separated by a comma
        for sz in sizes:
            result.append(str(sz))
            result.append(',')

        # Second portion of result will be a second type of delimiter
        result.append("#")

        # Last portion will be of the strings to be decoded
        result.extend(strs)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        # If string to be decoded is empty, return empty as decoded string
        if not s:
            return []

        # Size, result, and index to track decoding process
        sizes, res, i = [], [], 0

        # While the input does not equal the second delimiter, keep parsing through
        # the str, taking in the values as the sizes of the words to be decoded
        while s[i] != '#':
            j = i
            # While the input also does not equal the first delimited, append the integer to sizes
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        # Reach here once we reach the '#' which is to be parsed over 
        i += 1

        # For each value in sizes, we use that as the length of the string to accept next
        # and by retaining the index, we continue through the portion of the encoded string
        # where we are now at the part to be "decoded"
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res