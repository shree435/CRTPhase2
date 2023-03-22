class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None
class doubleLinkedList:
    def add_ele_beg(self,value,head):
        new_node=Node(value)
        new_node.next=head
        new_node.prev=None
        head=new_node
        return head
    def add_element(self,head,value):
        new_node=Node(value)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next=new_node
        new_node.prev=temp
    def print_list(self,head):
        temp=head
        while temp!=None:
            print(temp.data,end='->')
            temp=temp.next
        print()
    def print_reverse(self,head):
        temp=head
        while temp.next!=None:
            temp=temp.next
        while temp:
            print('<-',temp.data,sep='',end='')
            temp=temp.prev
        print()
    def insert_element(self, head, value, index):
        new_node = Node(value)
        cur = head
        pre = None
        while index != 0:
            pre = cur
            cur = cur.next
            index = index - 1
        pre.next = new_node
        new_node.next = cur
        new_node.prev = pre
        cur.prev=new_node
    def remove_node(self,head):
        temp=head
        while temp.next.next!=None:
            temp=temp.next
        temp.next.prev=None
        temp.next=None
obj=doubleLinkedList()
head=Node(10)
obj.add_element(head,20)
obj.add_element(head,30)
obj.add_element(head,40)
obj.print_list(head)
obj.print_reverse(head)
obj.remove_node(head)
obj.print_list(head)