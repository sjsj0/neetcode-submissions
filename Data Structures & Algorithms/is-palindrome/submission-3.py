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

        string=""
        for c in s:
            if c.isalnum():
                string += c.lower()

        return string == string[::-1]

        