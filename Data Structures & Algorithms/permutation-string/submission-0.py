class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        for c in s1:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        window = {}
        k = len(s1)

        for right in range(len(s2)):
            # add the new character on the right
            c = s2[right]
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            # drop the character falling off the left
            if right >= k:
                old = s2[right - k]
                window[old] -= 1
                if window[old] == 0:
                    del window[old]

            if window == need:
                return True

        return False