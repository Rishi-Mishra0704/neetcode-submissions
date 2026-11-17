class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)        # slowest possible speed, fastest needed speed
        answer = hi

        while lo <= hi:
            k = (lo + hi) // 2

            # Hours needed at speed k: each pile takes ceil(pile / k) hours
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k    # ceiling division without floats

            if hours <= h:
                answer = k        # k works, try slower
                hi = k - 1
            else:
                lo = k + 1        # too slow, go faster

        return answer