class Stack:
    arr=[]
    size=5
    def stack_push(self,ele):
        if len(self.arr)==self.size:
            print("Stack Overflow")
        else:
            self.arr.append(ele)
    def stack_pop(self):
        if len(self.arr)==0:
            print('Stack Underflow')
        else:
            self.arr.pop()
    def stack_peek(self):
        if len(self.arr)==0:
            print("Stack Underflow")
        else:
            print(self.arr[-1])
    def isEmpty(self):
        print(len(self.arr)==0)
s=Stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
print(s.arr)
s.stack_pop()
s.stack_pop()
s.stack_pop()
s.stack_pop()
print(s.arr)
s.stack_pop()
s.stack_peek()
s.isEmpty()