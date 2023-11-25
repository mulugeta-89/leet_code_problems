class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        sol_arr = []
        for email in emails:
            tempo = email.split("@")
            run = ""
            for item in tempo[0]:
                if item == ".":
                    continue
                if item == "+":
                    break
                run += item
            full = run+ "@" + tempo[1]
            sol_arr.append(full)
        return len(set(sol_arr))
        