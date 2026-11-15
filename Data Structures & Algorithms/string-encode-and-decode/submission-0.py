class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        position = 0
        while position < len(s):
            hash_index = position
            while s[hash_index] != "#":           # read the length digits
                hash_index += 1
            length = int(s[position:hash_index])
            start = hash_index + 1
            result.append(s[start:start + length])  # take exactly `length` characters
            position = start + length
        return result