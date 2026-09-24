class TimeMap:

    # 2 dict used to store value and timestamp
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

        return res



        # one dict implementation -----------------------------------------------
            # 2 dict used to store value and timestamp
    # def __init__(self):
    #     self.kv = {}

    # def set(self, key: str, value: str, timestamp: int) -> None:
    #     if key not in self.kv:
    #         self.kv[key] = []
    #     self.kv[key].append([value,timestamp])

    # def get(self, key: str, timestamp: int) -> str:
    #     if key not in self.kv:
    #         return ""
    #     arr = self.kv[key]
    #     res = ""

    #     l=0
    #     r=len(arr)-1
    #     while l<=r:
    #         mid = (l+r) // 2

    #         if arr[mid][1] <= timestamp:
    #             res = arr[mid][0]
    #             l = mid + 1
    #         elif arr[mid][1] > timestamp:
    #             r = mid - 1
    #         else:
    #             res = arr[mid][0]

    #     return res
