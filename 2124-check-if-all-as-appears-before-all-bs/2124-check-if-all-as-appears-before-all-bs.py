class Solution:
    def checkString(self, s: str) -> bool:
        s_dict = Counter(s)
        i = s_dict["a"] if "a" in s_dict else 0
        j = s_dict["b"] if "b" in s_dict else 0
        return (set(s[:i])) == {"a"} or (set(s[j-1:])) == {"b"}
        