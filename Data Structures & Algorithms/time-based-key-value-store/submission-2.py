class TimeMap:

    def __init__(self):
        self.kv = {}
        self.t = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = []
            self.t[key] = []

        self.kv[key].append(value)
        self.t[key].append(timestamp)

        print(self.kv)
        print(self.t)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.t:
            return ""
        arr = self.t[key]

        res = ""

        l=0
        r=len(arr)-1
        while l<=r:
            mid = (l+r) // 2

            if arr[mid] <= timestamp:
                res = self.kv[key][mid] 
                l = mid + 1
            elif arr[mid] > timestamp:
                r = mid - 1
            else:
                res = self.kv[key][mid] 
        timestamp -= 1

        return res



        # one dict implementation -----------------------------------------------
        
