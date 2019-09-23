class Solution:
    def isValid(self, s):
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in mapping:
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = '#'
                if not mapping[c] == top_element:
                    return False
            else:
                stack.append(c)
        return not stack


if __name__ == "__main__":
    solution = Solution()
    result = solution.isValid('((((()))))')
    print(result)
