
def defangIPaddr(self, address: str) -> str:
    updated = address.replace(".", "[.]")
    return updated