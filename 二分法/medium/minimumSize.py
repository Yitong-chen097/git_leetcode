"""
给你一个整数数组nums，其中nums[i]表示第i个袋子里球的数目。同时给你一个整数maxOperations。

你可以进行如下操作至多maxOperations次：

选择任意一个袋子，并将袋子里的球分到2 个新的袋子中，每个袋子里都有 正整数个球。
比方说，一个袋子里有5个球，你可以把它们分到两个新袋子里，分别有 1个和 4个球，或者分别有 2个和 3个球。
你的开销是单个袋子里球数目的 最大值，你想要 最小化开销。

请你返回进行上述操作后的最小开销。

示例 1：
输入：nums = [9], maxOperations = 2
输出：3
解释：
- 将装有 9 个球的袋子分成装有 6 个和 3 个球的袋子。[9] -> [6,3] 。
- 将装有 6 个球的袋子分成装有 3 个和 3 个球的袋子。[6,3] -> [3,3,3] 。
装有最多球的袋子里装有 3 个球，所以开销为 3 并返回 3 。

示例 2：
输入：nums = [2,4,8,2], maxOperations = 4
输出：2
解释：
- 将装有 8 个球的袋子分成装有 4 个和 4 个球的袋子。[2,4,8,2] -> [2,4,4,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,4,4,4,2] -> [2,2,2,4,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,4,4,2] -> [2,2,2,2,2,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2] 。
装有最多球的袋子里装有 2 个球，所以开销为 2 并返回 2 。

示例 3：
输入：nums = [7,17], maxOperations = 2
输出：7

提示：
1 <= nums.length <= 10**5
1 <= maxOperations, nums[i] <= 10**9

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

def minmumSize1(nums:List[int], maxOperations:int)->int:
  # 拍脑门写法
  result = []
  for j in range(maxOperations):
    if len(result) > 0:
      for j in range(len(result)):
        nums = result[j]
        mid = int(max(nums) / 2)
        for i in range(1, mid + 1):
          temp = List.copy(nums)  # 拷贝
          temp.append(i)
          temp.append(max(nums) - i)
          temp.remove(max(temp))
          if max(nums) >= max(temp):
            result[j] = temp
    else:
      mid = int(max(nums) / 2)
      for i in range(1, mid + 1):
        temp = List.copy(nums)  # 拷贝
        temp.append(i)
        temp.append(max(nums) - i)
        temp.remove(max(temp))
        result.append(temp)
  data = [max(_) for _ in result]
  return min(data)


def minmumSize(nums:List[int], maxOperations:int)->int:
  # 二分法
  def operate_times(mid) -> int:
    """
    统计开销次数
    """
    count = 0
    for item in nums:
      if item > mid:
        count += int((item-1)/mid)
    #     拆分次数分 偶数拆分 和 奇数拆分
    return count


  # 边界值
  left = 1
  right = max(nums)
  # 中间值
  while left <= right:
    mid = int((left + right) / 2)
    if operate_times(mid) <= maxOperations:
      right = mid - 1
    else:
      left = mid + 1
  return left


if __name__=="__main__":
  nums = [2,4,8,2]
  maxOperations = 4
  print(minmumSize(nums, maxOperations))