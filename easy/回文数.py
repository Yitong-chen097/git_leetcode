"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。
 
示例 1：
输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
提示：
-2**31 <= x <= 2**31 - 1
进阶：你能不将整数转为字符串来解决这个问题吗？
"""
# def isPalindrome(x:int)->bool:
#   if x < 0:
#     return False
#   else:
#     length = len(str(x))
#     for i in range(length):
#       # 拍脑门方法
#       if str(x)[i] != str(x)[length - i - 1]:
#         return False
#     return True

# def isPalindrome(x:int)->bool:
#   # 翻转字符串
#   return str(x)==str(x)[::-1]

def isPalindrome(x:int)->bool:
  # 数学方法翻转字符串
  if x < 0:
    return False
  else:
    y = 0
    item = x
    while x:
      y = y * 10 + x % 10 
      x = x // 10
    return y == item


if __name__=="__main__":
  print(isPalindrome(1221))