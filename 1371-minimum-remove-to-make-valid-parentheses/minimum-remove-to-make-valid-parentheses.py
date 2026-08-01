class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        OPENING, CLOSING = "(", ")"
        stack = []
        s = list(s)

        for i, ch in enumerate(s):
            if ch == OPENING:
                stack.append(i)
            elif ch == CLOSING:
                if not stack:
                    s[i] = ""
                else:
                    stack.pop()

        for extra_i in stack:
            s[extra_i] = ""

        return "".join(s)