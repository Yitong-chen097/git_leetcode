"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]
 
提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


# class LinkList:
#   def __init__(self):
#     self.head = None
#
#   def initLinkList(self, data):
#     # 创建 链表
#     # 头结点
#     self.head = ListNode(data[0])
#     r = self.head
#     p = self.head
#     # 循环创建各个结点
#     for i in data[1:]:
#       node = ListNode(i)
#       p.next = node
#       p = p.next
#     return r
#
#   def printList(self, head):
#     # 打印链表
#     if head == None:
#       return
#     node = head
#     while node != None:
#       print(node.val, end=' ')
#       node = node.next


class Solution:
  def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 法一：迭代
    # 这个方法之前自己也试着做 然后一直卡壳 原因在于 循环整错了 我可真是醉了
    result_list = ListNode()
    r = result_list
    while list1 and list2:
      # 时间复杂度 O(length(list1) + length(list2))
      if list1.val <= list2.val:
        r.next = list1
        list1 = list1.next
      else:
        r.next = list2
        list2 = list2.next
      r = r.next
    r.next = list1 if list1 is not None else list2   #将其中一个还没有结束的链表直接拼接在最后
    return result_list.next

  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 法二：递归
    # 这个方法想了一半 时间复杂度也是 O(length(list1) + length(list2))
    if list1 is None:
      return list2
    elif list2 is None:
      return list1
    elif list1.val < list2.val:
      list1.next = self.mergeTwoLists(list1.next, list2)
      return list1
    else:
      list2.next = self.mergeTwoLists(list1, list2.next)
      return list2


if __name__ == "__main__":
  # l = LinkList()
  l1 = ListNode()
  list1 = l1
  for i in range(1,4):
    l1.val = i
    l1.next = ListNode()
    l1 = l1.next
  l1.val = 4

  l2 = ListNode()
  list2 = l2
  for i in range(1, 8, 2):
    l2.val = i
    l2.next = ListNode()
    l2 = l2.next
  l2.val = 9

  result_list = Solution().mergeTwoLists(list1, list2)
  while result_list!=None:
    print(result_list.val, end=' ')
    result_list = result_list.next