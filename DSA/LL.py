class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class likelist:
    def __init__(self):
        self.head=None
    def create(self):
        n=int(input("Enter how many records: "))
        for i in range(n):
            data=int(input("Enter the data:"))
            newnode=Node(data)
            if self.head is None:
                self.head=newnode
                temp=self.head
            else:
                temp.next=newnode
                tem=newnode
                temp=temp.next

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data, end="->")
            temp=temp.next
        print("None")
ll=likelist()
ll.create()
ll.display()