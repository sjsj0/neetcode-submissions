class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for t in tasks:
            count[t] +=1

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time=0
        queue = deque()  ## pairs of [-cnt, time at which it can be accepted]

        while maxHeap or queue:
            time += 1

            if not maxHeap:
                time = queue[0][1]  ## directly jump the time counter to the value in queue
            else:
                cnt = 1 + heapq.heappop(maxHeap)      ## it gives -ve value so to reduce by 1, add it
                if cnt:
                    queue.append([cnt, time+n])     ## time+n becoz time is inc by 1 and after n waits it can be accepted..

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time



