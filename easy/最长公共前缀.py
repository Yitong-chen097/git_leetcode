"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
 
提示：
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
"""
from typing import List


def longsetCommonPrefix(strs:List[str])->str:
  result = ''
  strs = sorted(strs, key=len)
  flag = True
  for i in range(len(strs[0])):
    for v in strs[1:]:
      if v[i] != strs[0][i]:
          flag = False
          break
    if flag:
      result += strs[0][i]
  return result


if __name__=="__main__":
  strs = ["flower","flow","light"]
  print(longsetCommonPrefix(strs))