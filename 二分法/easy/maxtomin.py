"""

一座有n（2<=n<=100000）间牛舍的小屋，牛舍排在一条直线上，第i间牛舍在xi（0<=xi<=1000000000）的位置。。
一共有c头牛，为了防止牛之间互相攻击互相伤害，因此决定把每头牛都放在离其它牛尽量远的牛舍，
使任意两头牛之间的最小距离尽可能大，那么，这个最大的最小距离是多少呢？
例如 输入：(3,[1,2,8,4,9])，输出：3

解释：3代表3头牛，列表[1,2,8,4,9]代表五间牛舍的位置。
把三头牛分别放在位置是1，4，8或1，4，9的牛舍时，它们间隔的最小距离最大，是3


最大化最小值的题目，采用二分法
"""


def toResult(n, l):

  def operate_times(mid):
    """
    开销函数
    """
    pos = l[0]
    count = 1
    for i in range(len(l)):
      if l[i] - pos >=mid:
        count += 1
        pos = l[i]


    return count

  left = 1
  right = (max(l) - min(l))//(n-1)
  while left <= right:
    mid = (left + right) // 2
    if operate_times(mid) < n:
      right = mid - 1
    else:
      left = mid + 1
  return right


if __name__ == "__main__":
  n = 3
  l = [1, 2, 8, 4, 9]

  print(toResult(n, sorted(l)))
