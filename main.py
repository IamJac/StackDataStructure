import stackclass as st
from time import sleep
obj=st.Stack()
option=None
value=None
num_delete=None
element_index=None
index=None
while option!=0:
    print()
    print("Choose an operation from the Menu below")
    print("Input 0 to exit")
    print("")
    print("1.Add elements into the stack")
    print("2.Remove elements from the stack")
    print("3.Count of elements in the stack")
    print("4.Display stack elements")
    print("5.Check element stored in a certain position")
    option=int(input("Your option"))
    if option==1:
        value=int(input("Enter an integral value to be stored in the stack"))
        obj.push(value)
        sleep(1)
        print()
    elif option==2:
        num_delete=int(input("Input element to be deleted"))
        element_index=obj.pop(num_delete)
        if element_index!=-1:
            print(F"The value {num_delete} which was at position {element_index} of the stack has been removed successfully")
        else:
            print("Stack underflow-The stack is empty")
        sleep(1)
        print()
    elif option==3:
        print(f'The stack has {obj.count()} elements')
        sleep(1)
        print()
    elif option==4:
        obj.display()
        sleep(1)
        print()
    elif option==5:
        index=int(input("Input stack position of the element to be checked"))
        obj.peek(index)
        sleep(1)
        print()
    else:
        print(F"{option} is an invalid option.Input a proper one")
        sleep(1)
        print()
