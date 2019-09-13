# 栈空间
用来存储当前格子向4个方向的搜索状态
# DFS特点
需要回溯
# 列表生成式
```
list = [['X' for _ in range(n)] for _ in range(m)]
```
指代的含义：
```
list = []
for _ in range(n):
    templist = []
    for _ in range(m):
        templist.append('X')
list.append(templist)

```
也即：
生成一个n×m的矩阵，每个元素都是'X'

其中
>for _ in range(n):

中的“_”相当于each，指代循环中的变量