class TimeMap:
    def __init__(self):
        self.store = {}   # key -> list of (timestamp, value), timestamps increasing

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # LeetCode guarantees set() timestamps for a key strictly increase,
        # so appending keeps each list sorted by timestamp
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        entries = self.store[key]
        result = ""
        lo, hi = 0, len(entries) - 1

        # Binary search for the latest timestamp <= the requested timestamp
        while lo <= hi:
            mid = (lo + hi) // 2
            if entries[mid][0] <= timestamp:
                result = entries[mid][1]   # valid candidate, but try to find a later one
                lo = mid + 1
            else:
                hi = mid - 1               # too new, look earlier

        return result