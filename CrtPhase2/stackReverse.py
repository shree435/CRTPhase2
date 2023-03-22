class Stack:
    def __init__(self):
        self.arr=[]
    def stack_push(self,ele):
        self.arr.append(ele)
    def stack_pop(self):
        return self.arr.pop()
    def stack_peek(self):
        return self.arr[-1]
    def print_stack(self):
        print(self.arr)
s1=Stack()
s1.stack_push(1)
s1.stack_push(2)
s1.stack_push(3)
s1.stack_push(4)
s1.stack_push(5)
s1.print_stack()
s2=Stack()
s2.stack_push(s1.stack_pop())
s2.stack_push(s1.stack_pop())
s2.stack_push(s1.stack_pop())
s2.stack_push(s1.stack_pop())
s2.stack_push(s1.stack_pop())
s2.print_stack()
