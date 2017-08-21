# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:42:40 2017

@author: shsubram
"""
class longestPalindrome:
    def __init__(self,s):
        self.s = s
        self.longest = ''
        self.memo = [None] * len(s)
        for _ in range(len(s)):
            self.memo[_] = [None] * len(s)
    def getLongestPalindromicSubString(self):
        self.longestPalindromicSubString(self.s,0,len(self.s)-1)
        if self.s and len(self.longest) <= 1:
            self.longest = self.s[-1]
        return self.longest
    def longestPalindromicSubString(self,s,start,end):
        if self.s == "":
            return False
        elif len(self.s) == 1:
            self.longest = self.s
        elif start >= end:
            self.memo[start][end] = True
        elif len(s[start:end+1]) == 1:
            self.memo[start][end] = True
            if len(self.longest) <= 1:
                self.longest = self.s[start]
        elif len(s[start:end+1]) == 2:
            if s[start] == s[end]:
                self.memo[start][end] = True
                if len(self.longest) <= 1:
                    self.longest = self.s[start:end+1]
            else:
                self.memo[start][end] = False
        else:
            for i in range(start,end):
                for j in range(end,start-1,-1):
                    if self.memo[i+1][j-1] == None:
                       self.longestPalindromicSubString(s,i+1,j-1)
                    if self.memo[i+1][j-1] and s[i] == s[j]:
                        self.memo[i][j] = True
                        if len(self.longest) < len(self.s[i:j+1]):
                            self.longest = self.s[i:j+1]
                    else:
                        self.memo[i][j] = False
try:
    myStr = input("Enter a string:\n")
    if type(myStr) != str:
        raise TypeError("Entered input is not a string")
    myClass = longestPalindrome(myStr)
    palindrome = myClass.getLongestPalindromicSubString()  
    if palindrome:
        print "Longest palindrome in %s is %s."%(myStr,palindrome)
    else:
        print "Entered string has no palindromic substring."
except TypeError as err:
    print "Exception caught: ", err.args[0]
except:
    print "Unknow error occured, can't proceed."
    
    
      
