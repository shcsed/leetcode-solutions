class Solution:
    def isValid(self, s: str) -> bool:
        opened = {
            "(": 0,
            "[": 0,
            "{": 0,
        }
        current_parens = []
        for c in list(s):
            if c in ("(", "[", "{"):
                opened[c] += 1
                current_parens.append(c)
            if c in (")", "]", "}"):
                if len(current_parens) < 1:
                    return False
                if c == ")":
                    if current_parens[-1] != "(":
                        return False
                    else:
                        opened[current_parens[-1]] -= 1
                        current_parens.pop()
                if c == "]":
                    if current_parens[-1] != "[":
                        return False
                    else:
                        opened[current_parens[-1]] -= 1
                        current_parens.pop()
                if c == "}":
                    if current_parens[-1] != "{":
                        return False
                    else:
                        opened[current_parens[-1]] -= 1
                        current_parens.pop()
        return not any(opened.values())
