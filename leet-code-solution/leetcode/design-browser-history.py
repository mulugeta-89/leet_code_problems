class Node:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.back = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        

    def visit(self, url: str) -> None:
        will_be_visited = Node(url)
        self.head.next = will_be_visited
        will_be_visited.back = self.head
        self.head = will_be_visited
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.head.back:
                self.head = self.head.back
            else:
                break
        return self.head.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.head.next:
                self.head = self.head.next
            else:
                break
        return self.head.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)