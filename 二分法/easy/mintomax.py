"""
给定的一个长度为N的正整数数组，现要将其截成M(M≤N)段，要求每段数组和的最大值最小。例如 输入：([4,2,4,5,1], 3) 输出：6

最小化最大值的题目，采用二分法
"""



def toResult(m,n):

  def operate_times(mid):
    """
    开销函数
    """
    sum = 0
    count = 0
    for i in range(len(m)):
      sum += m[i]
      if sum > mid:
        count += 1   #段数加1
        sum = m[i]  #将sum初始化成下一段要统计的初始数字
    return count
    pass

  # 确定左右边界  !!!!!!!!
  left = max(m)
  right = sum(m)
  while left <= right:
    mid = (left + right) // 2
    if operate_times(mid) <= n:
      right = mid - 1
    else:
      left = mid + 1
  return left


if __name__=="__main__":
  m = [4,2,4,5,1]
  n = 3
  print(toResult(m,n))