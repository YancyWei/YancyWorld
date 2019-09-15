from queue import Queue


class Solution:
    def numSquares(self, n: int):
        visited = set()
        collection = []  # 平方数集
        # 生成平方数
        for i in range(1, n+1):
            sqr = i**2
            if sqr <= n:
                collection.append(sqr)
            else:
                break
        # 生成队列，初始化结点
        queue = Queue()
        queue.put((0, 0))
        # 进入队列
        while not queue.empty():
            node, step = queue.get()
            step += 1
            for num in collection:
                num += node
                if num == n:
                    return step
                if num < n and (num, step) not in visited:
                    queue.put((num, step))
                    # 不满足条件的结点加入黑名单，防止重复，该问题结点包括求和数和所需步数
                    visited.add((num, step))
        return 0


if __name__ == "__main__":
    n = 13
    solution = Solution()
    result = solution.numSquares(n)
    print(result)
