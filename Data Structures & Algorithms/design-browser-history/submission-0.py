class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.node=Node(homepage)
        
        

    def visit(self, url: str) -> None:
        new_node=Node(url)
        self.node.next=new_node
        new_node.prev=self.node
        self.node= self.node.next

        

    def back(self, steps: int) -> str:
        while self.node.prev and steps > 0 :
            self.node=self.node.prev
            steps-=1
        return self.node.val
        

    def forward(self, steps: int) -> str:
        while self.node.next and steps > 0:
            self.node=self.node.next
            steps-=1
        return self.node.val        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)