class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string=""
        # for i in range(len(s)):
        #     if s[i] not in " `~!@#$%^&*():;'\"?><,.|\\":
        #         string += s[i].lower()
        
        # print(string)
        # l=len(string)
        # for i in range(int(l/2)):
        #     if string[i] != string[l-1-i]:
        #         return False

        # return True

        # ----------------------
        # string=""
        # for c in s:
        #     if c.isalnum():
        #         string += c.lower()

        # return string == string[::-1]
        # ----------------------

        l=0
        r=len(s)-1

        while l<r:
            while l<r and not self.isAlphaNum(s[l]):
                l+=1
            while l<r and not self.isAlphaNum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True


    def isAlphaNum(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or 
                (ord('a') <= ord(c) <= ord('z')) or 
                (ord('0') <= ord(c) <= ord('9')))

        