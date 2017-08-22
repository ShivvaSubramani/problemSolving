class Solution(object):
    def getCount(self,x):
        count = 0
        while True:
            count += 1
            x = x/10
            if not x:
                break
        return count
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if type(x) != int:
            print "Error: input has to be an integer"
            return
        if x == 0:
            return True
        elif x < 0:
            return False        
        count = self.getCount(x)
        if count == 1:
            return True
        divider = 1*pow(10,count-1)
        num1 = None
        while divider:
            if num1 == None:
                num1 = x/divider
            num2 = x % 10
            if num1 != num2:
                return False
            count -= 2
            x = (x % divider)/10
            if self.getCount(x) != count:
                num1 = 0  
            else:
                if count == 1:
                    break
                num1 = None
            divider = divider/100
        return True
        
myclass = Solution()
print myclass.isPalindrome(0101)