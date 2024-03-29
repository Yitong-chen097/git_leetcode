"""
最小路径和

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，
使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例 1：
1  3  1
1  5  1
4  2  1
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12


提示：
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


def minPathSum(a):
  """
  要求最小路径和需明白：
  前面的累和 + 最后的a[i][j]最小  (设i j是循环因子，现在因子走到最后)
  而到达a[i][j]只有两种途径 一种是从a[i-1][j]走下来 一种是a[i][j-1]从左走过来
  也就是说 最后的最小值 一定是 minSum = a[i][j] + min(a[i-1][j], a[i][j-1])
  两种方式里面哪一个最小 加上 最后的值肯定最小

  逆推发现：
  走到最前面
  要么到达最左处 要么到达最上处封顶
  最左处和最上处 已经没有左和上 可以 从左到右过来 和 从上到下过来
  所以初始值就是
  最左处 和 最上处

  二维数组中 最左处是 第0列
  最上处是 第0行 需要都初始
  """
  row = len(a)
  col = len(a[0])
  for i in range(row):
    for j in range(col):
      # 初始化最上处:只能从左边过来
      if i == 0 and j != 0:
        a[0][j] += a[0][j - 1]
      # 初始化最左处:只能从上面过来
      if j == 0 and i != 0:
        a[i][0] += a[i - 1][0]
      # 不是最上和最左
      if i > 0 and j > 0:
        a[i][j] += min(a[i - 1][j], a[i][j - 1])
  return a[row - 1][col - 1]


if __name__ == '__main__':
  grid = [[1, 2, 3], [4, 5, 6]]
  print(minPathSum(grid))
