class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix=[1]
        # pseudoSuffix=[1]

        # l=len(nums)
        # for i in range(1,l):
        #     prefix.append(prefix[-1]*nums[i-1])
        #     pseudoSuffix.append(pseudoSuffix[-1]*nums[l-i])

        # suffix=pseudoSuffix[::-1]
        # ans=[]
        # for i in range(l):
        #     ans.append(prefix[i]*suffix[i])

        # return ans

        ans=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix=1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans