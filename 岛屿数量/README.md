# 参考教程
[点这里](https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/)
# 栈空间
用来存储当前格子向4个方向的搜索状态
```python {.line-numbers}
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
```
    #        x-1,y
    # x,y-1    x,y      x,y+1
    #        x+1,y
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量，这是一个常见的技巧
# DFS和BFS区别
DFS是深度搜索，需要回溯
BFS是广度搜索，利用队列的方法直接铺开
# 列表生成式
```python {.line-numbers}
list = [['X' for _ in range(n)] for _ in range(m)]
```
## 指代的含义：
```python {.line-numbers}
list = []
for _ in range(m):
    templist = []
    for _ in range(n):
        templist.append('X')
list.append(templist)
```
也即：
生成一个m×n的矩阵，每个元素都是'X'

其中
```python {.line-numbers}
for _ in range(n):
```
中的“_”相当于each，指代循环中的变量