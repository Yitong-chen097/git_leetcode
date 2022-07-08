"""
回文数
 
示例 1：
输入：x = 121
输出：true

示例 2：
输入：x = -121
输出：false

示例 3：
输入：x = 10
输出：false

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

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