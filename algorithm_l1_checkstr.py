'''
描述

查找字符串

'''

class Solution:
    def checkStr(self,source, target):
        if ( (source is None) or (target is None) ):
            return -1
        _sourcelen,  _targetlen = len(source), len(target)

        for i in range(_sourcelen - _targetlen + 1 ):
            for j in range(_targetlen):
                if source[i + j] != target[j]:
                    break
            else:
                return i
        return -1

s=Solution()
print(s.checkStr('source','rce'))