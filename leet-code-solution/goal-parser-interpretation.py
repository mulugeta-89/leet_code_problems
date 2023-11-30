class Solution:
    def interpret(self, command: str) -> str:
        sol = ""
        for i in range(len(command)-1):
            if command[i] == "G":
                sol += "G"
            elif command[i] == "(" and command[i+1]  == ")":
                sol += "o"
            elif command[i] == "(" and command[i+1]  == "a":
                sol += "al"
        if command[len(command)-1] == "G":
            sol += "G"
        return sol
        