class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Stack ---------------------------------------
        # position, speed = zip(*sorted(zip(position, speed), reverse=True))
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda x: x[0], reverse=True)
        position, speed = zip(*pairs)


        dist = [target - p for p in position]
        time = [dist[i] / speed[i] for i in range(len(position))]
        print(time)

        stack=[]
        for t in time:
            stack.append(t)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        print(stack)
        return len(stack)

        # # written better
        # pairs = [(p,s) for p,s in zip[(position,speed)]
        # pairs.sort(reverse=True)
        # stack = []

        # for p,s in pair:
        #     stack.append((target-p)/s)
        #     if len(stack)>=2 and stack[-1]<=stack[-2]:
        #         stack.pop()
        # return len(stack)
