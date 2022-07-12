"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true

提示：
1 <= s.length <= 10**4
s 仅由括号 '()[]{}' 组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# from typing import ParamSpecArgs


def isValid(s:str)->bool:
  # dict_valid = {"(":")", "[":"]", "{":"}"}
  # flag = False
  # if len(s)%2 == 0:
  #   for i in range(len(s)):
  #     if i+1<len(s) and dict_valid.get(s[i]) == s[i+1] or i<int(len(s)/2) and dict_valid.get(s[i]) == s[len(s)-i-1]:
  #       有问题 只考虑两种情况 忽略第三种"()[{}]"
  #       flag = True
  #     else:
  #       flag = False
  # return flag
  """最优的栈做法:左括号进栈 匹配到右括号出栈 全部出栈说明是完全匹配"""
  if len(s)%2 != 0:
    return False
  dict_valid = {"}":"{",")":"(","]":"["}
  stack = list()
  for v in s:
    if v in dict_valid:
      if len(stack)!=0 and stack[-1] == dict_valid.get(v):
        stack.pop()
    else:
      stack.append(v)
  return not stack

if __name__=="__main__":
  s = "[]{(}}"
  print(isValid(s))