# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 14:33:07 2017

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
        return self.longest
    def longestPalindromicSubString(self,s,start,end):
        if self.s == "":
            return False
        elif len(self.s) == 1:
            self.longest = self.s
        elif start >= end:
            self.memo[start][end] = True
            return True
        elif len(s[start:end+1]) == 1:
            self.memo[start][end] = True
            if self.longest == "":
                self.longest = self.s[start]
            return True
        elif len(s[start:end+1]) == 2:
            if s[start] == s[end]:
                self.memo[start][end] = True
                if len(self.longest) <= 1:
                    self.longest = self.s[start:end+1]
                return True
            else:
                self.memo[start][end] = False
                return False
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
                
myClass = longestPalindrome("baabaaaa")
print myClass.getLongestPalindromicSubString()        
