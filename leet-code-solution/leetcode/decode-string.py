class Solution:
    def decodeString(self, s: str) -> str:
        curr_num = ""
        num_str = ""
        stack = []
        for item in s:
            if item.isnumeric():
                curr_num+=item
            elif item == "[":
                stack.append(num_str)
                stack.append(int(curr_num))
                num_str = ""
                curr_num = ""
            elif item == "]":
                num = stack.pop()
                stri = stack.pop()
                num_str = stri + num*num_str
            else:
                num_str += item
        return num_str