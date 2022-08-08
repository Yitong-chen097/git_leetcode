"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 
提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10**6 <= nums1[i], nums2[i] <= 10**6

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


def findMedianSortedArrays(nums1:List[int], nums2:List[int])->float:
  """
  如果采用传统的根据数组长度奇偶来判断中位数 导致的时间复杂度和空间复杂度都为O(m+n)
  不符合我们的要求
  一般涉及到这种类型的题目还要log的时间复杂度基本要使用二分法
  """
  

  nums = sorted(nums1 + nums2)
  left = 0
  right = len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    pass
  pass


if __name__=="__main__":
  nums1 = [1,3]
  nums2 = [2]
  print(findMedianSortedArrays(nums1=nums1,nums2=nums2))