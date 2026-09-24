class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = [0]+nums
        for i in range(2,len(self.arr)):
            self.insert(i)

        print(f'init:{self.arr}')


    def add(self, val: int) -> int:
        self.arr.append(val)
        self.insert(len(self.arr)-1)
        print(f'after adding:{self.arr}')

        tempArr = self.arr.copy()
        for i in range(self.k):
            self.delete(len(self.arr)-1 - i)
            print(f'after {i+1} delete:{self.arr}')

        res = self.arr[-self.k]

        self.arr = tempArr
        print(f'after assigning:{self.arr}')
        return res




    def insert(self, n):
        temp = self.arr[n]

        i = n
        while i>1 and temp > self.arr[i//2]:
            self.arr[i] = self.arr[i//2]
            i=i//2
        self.arr[i]=temp

    def delete(self, n):
        temp = self.arr[1]
        self.arr[1] = self.arr[n]
        i=1
        j=2*i
        while j <= n-1:
            if self.arr[j+1] > self.arr[j]:
                j=j+1
            if self.arr[i] < self.arr[j]:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i=j
                j=2*i
            else:
                break

        self.arr[n] = temp


