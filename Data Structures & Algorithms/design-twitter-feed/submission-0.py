class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        data = [self.counter, tweetId]
        self.counter -= 1       ## the more -ve the more latest the post is
        self.tweetMap[userId].append(data)

    def getNewsFeed(self, userId: int) -> List[int]:
        
        res = []
        minHeap = []
        
        self.followMap[userId].add(userId)      ## add yourself in your followers list
        for fId in self.followMap[userId]:
            if fId in self.tweetMap:
                for tweet in self.tweetMap[fId]:
                    heapq.heappush(minHeap, tweet)

        while minHeap and len(res) < 10:
            count, tweetId = heapq.heappop(minHeap)
            res.append(tweetId)

        return res





    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
