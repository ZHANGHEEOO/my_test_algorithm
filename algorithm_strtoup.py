'''
描述

将一个字符由小写字母转换为大写字母

'''

class Solution:
    """
    @param character: a character
    @return: a character
    """
    def lowercaseToUppercase(self, character):
        # write your code here
        string = str.upper(character)
        return string

s = Solution()
_str = s.lowercaseToUppercase('this is a str')
print(_str)