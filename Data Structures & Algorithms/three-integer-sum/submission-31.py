class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Brute Force
        # ans=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 temp=sorted([nums[i],nums[j],nums[k]])
        #                 if temp not in ans:
        #                     ans.append(temp)
        
        # return ans

        nums.sort()
        # print(nums)
        ans=[]
        # if nums==[0,0,0]:
        #     return [nums]
        hashMap=defaultdict(set)
        for i in range(len(nums)):
            hashMap[nums[i]].add(i)

        print(f'hashMap={hashMap}')

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                diff = 0-(nums[i]+nums[j])
                if diff in hashMap:
                    indices=hashMap[diff]
                    print(diff, indices, i ,j)
                    if (i not in indices and j not in indices) or ((i in indices or j in indices) and len(indices)>2) :
                        temp=sorted([nums[i],nums[j],diff])
                        print(f'temp={temp}')
                        if temp not in ans:
                            ans.append(temp)
                else:
                    hashMap[nums[i]].add(i)
                    hashMap[nums[j]].add(j)
        
        return ans


        