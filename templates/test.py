class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return 1
        else:
        
            return(helper(countAndSay(n-1)))

    def helper_array(self, n):
        num = n
        res = list()
        counter = 1
        print("len(num)",len(num))


        for i in range(len(num)):

            if (i < len(num) - 1) and num[i] == num[i+1]:
                counter = counter + 1

            else:
                res.append([num[i],counter])
                counter = 1

        return res

    def helper_puttogether(self, nums):
        res = ""
        for i in range(len(nums)):
            res = res + str(nums[i][0]*nums[i][1])

        return res


s = Solution()

print(s.helper_puttogether(s.helper_array("223314444411")))
