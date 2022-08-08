""""
给定一个由 0 和 1 组成的矩阵 mat，请输出一个大小相同的矩阵，
其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

示例 1：
 0 0 0
 0 1 0
 0 0 0

输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]

示例 2：
 0 0 0
 0 1 0
 1 1 1

输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
输出：[[0,0,0],[0,1,0],[1,2,1]]

提示：
m == mat.length
n == mat[i].length
1 <= m, n <= 10**4
1 <= m * n <= 10**4
mat[i][j] is either 0 or 1.
mat 中至少有一个 0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/2bCMpM
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from collections import deque

def updateMatrix1(mat:List[List[int]]) -> List[List[int]]:
  """
     自己写的暴力：
     存储0的位置 存储1的位置 初始化结果矩阵
     然后将1的位置不断和各个0的位置进行比较拿距离来更新矩阵
  """
  result = [ [0] * len(mat[0]) for _ in range(len(mat)) ] #初始化结果矩阵
  position_zero = []  #记录0的位置
  position_one = []   #记录1的位置
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      if mat[i][j] == 1:  # 1
        position_one.append([i,j])
      else:
        position_zero.append([i,j])
  # 更新结果矩阵
  for p_o in position_one:
    length = []
    for p_z in position_zero:
      if p_o[0] == p_z[0] or p_o[1] == p_z[1]:
        length.append(abs(sum(p_o) - sum(p_z)))
      else:
        length.append(abs(p_o[0]-p_z[0])+abs(p_o[1]-p_z[1]))
    result[p_o[0]][p_o[1]] = min(length)
  return result

def updateMatrix(mat:List[List[int]]) -> List[List[int]]:
  # leetcode 广度优先算法 应该多次回顾这道题
  rows, cols = len(mat), len(mat[0])
  # 初始化结果矩阵
  result = [[0] * cols for _ in range(rows)]
  # 0的位置
  position_zero = [(i,j) for i in range(rows) for j in range(cols) if mat[i][j]==0]
  # 初始化队列:先进先出 First in First out
  q = deque(position_zero)   #将所有0的位置入队
  unique_items = set(position_zero)   # 防止重复添加元素, 元素唯一

  while q:
    #   当队列不为空的时候，为空说明已经全部出列或者说已经遍历完成
    #   取出第一个元素
    q_i, q_j = q.popleft()
    #   逐层遍历元素:矩阵中 只有上下左右
    for i, j in [(q_i, q_j + 1), (q_i, q_j - 1), (q_i + 1, q_j), (q_i - 1, q_j)]:
      if 0 <= i < rows and 0 <= j < cols and (i,j) not in unique_items:
        result[i][j] = result[q_i][q_j] + 1  #存储的是距离
        # 将访问的元素加入队列和set(防止重复添加)
        q.append((i,j))
        unique_items.add((i,j))


  return result

if __name__=="__main__":
  mat = [[0,0,0],[0,1,0],[1,1,1]]
  print(updateMatrix(mat))