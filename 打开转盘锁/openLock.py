from typing import List
from queue import Queue


class Solution:
    def openLock(self, deadends: List[str], target: str):
        deadends = set(deadends)  # 无序、不重复数集
        if '0000' in deadends:
            return -1

        # 生成队列，初始化结点
        queue = Queue()
        queue.put(('0000', 0))

        while not queue.empty():
            # 取出结点
            node, step = queue.get()
            # 4位密码
            for i in range(4):
                # 上、下两种转法
                for add in (1, -1):
                    # 转动后的数字
                    cur = node[:i] + str((int(node[i]) + add) %
                                         10) + node[i+1:]
                    if cur == target:
                        return step + 1
                    if cur not in deadends:
                        queue.put((cur, step + 1))  # 将转动厚的数字加入队列中
                        deadends.add(cur)  # 更新死亡数字避免重复
        return -1


if __name__ == '__main__':
    deadends = ["0201"]
    target = "0000"
    solution = Solution()
    result = solution.openLock(deadends, target)
    print(result)
