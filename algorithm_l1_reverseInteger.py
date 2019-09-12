'''
描述

反转一个只有3位数的整数

'''

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        number = int(number)
        if ( (number < 100) or (number >= 1000) ):
            return 'check the number length'
        _list = list( str(number) )
        revlist = _list[::-1]
        revstr = ''.join(revlist)
        new_num = int(revstr)
        return new_num


s = Solution()
_str = s.reverseInteger(123456)
print(_str)