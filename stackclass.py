class Stack:
    def __init__(self):
        self.array_capacity=10
        self.data=[]
    def count(self):
        return len(self.data)
    def push(self,value):
        if len(self.data)==0:
            self.data.append(value)
            print(F"The value {value} has been successfully pushed into the stack")
            return
        elif len(self.data)==self.array_capacity:
            print("Stack overflow-The stack is full")
            return
        else:
            self.data.append(value)
            print(F"The value {value} has been successfully pushed into the stack")
            return
    def pop(self,value1):
        if self.array_capacity==0:
            return -1
        else:
            for t in range(0,len(self.data),1):
                if value1==self.data[t]:
                    self.data.remove(value1)
                    return t

    def peek(self,pos):
        for w in range(0,len(self.data),1):
            if pos==w:
                print(F"The element at index {pos} of the stack is {self.data[w]}")
                return
        else:
            print(F"The index {pos} is out of bounds")
            return

    def display(self):
        if len(self.data)==0:
            print("The stack is empty")
            return
        else:
            num=-1
            print("Stack elements:-")
            while num>=-(len(self.data)):
                print(self.data[num],end=" ")
                num-=1
            return
