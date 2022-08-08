"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

示例 1：
Start []  []  []  []  []  []
  []  []  []  []  []  []  []
  []  []  []  []  []  []  Finish
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6

提示：
    1 <= m, n <= 100
    题目数据保证答案小于等于 2 * 10**9

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

def uniquePaths(m:int, n:int)->int:
  dp = [[1 for _ in range(n)] for _ in range(m)]
  dp[0][0] = 0
  for i in range(m):
    for j in range(n):
      #初始化最上值 只能从左往右 所以每个格子都只有1种能到达
      if i == 0 and j != 0:
        dp[0][j] = 1
      #初始化最左值 只能从上到下 所以每个格子都只有1种能到达
      if j ==0 and i != 0:
        dp[i][0] = 1
      # 中间位置的推导计算
      if i>0 and j>0:
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
  return dp[m-1][n-1]

if __name__=='__main__':
  m = 3
  n = 3
  print(uniquePaths(m,n))