class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position, speed = zip(*sorted(zip(position, speed), reverse=True))
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda x: x[0], reverse=True)
        position, speed = zip(*pairs)


        dist = [target - p for p in position]
        time = [dist[i] / speed[i] for i in range(len(position))]
        print(time)

        stack=[]
        for t in time:
            if stack and stack[-1] < t:
                stack.append(t)
            elif not stack:
                stack.append(t)
        
        print(stack)
        return len(stack)
