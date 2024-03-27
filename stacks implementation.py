s = []
top = None

def isempty(stk):
    return len(stk) == 0

def push(stk, item):
    stk.append(item)
    global top
    top = len(stk) - 1

def s_pop(stk):
    global top
    if isempty(stk):
        return "underflow!"
    else:
        i = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = top - 1
        return i

def peek(stk):
    if isempty(stk):
        return "underflow!"
    else:
        return stk[top]

def display(stk):
    if isempty(stk):
        print("stack is empty")
    else:
        print(stk[top], "<-- top")
        for i in range(top - 1, -1, -1):
            print(stk[i])

while True:
    print("STACK IMPLEMENTATION")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = input("Enter the choice (1-5): ")

    if ch == '1':
        item = int(input("Enter the item you want to push: "))
        push(s, item)
        print("%d added successfully" % item)
        input("Press any key to continue...")

    elif ch == '2':
        item = s_pop(s)
        if item == 'underflow!':
            print("Underflow! Stack is empty!")
        else:
            print("%d is popped" % item)
        input("Press any key to continue...")

    elif ch == '3':
        item = peek(s)
        if item == 'underflow!':
            print("Underflow! Stack is empty!")
        else:
            print("%d is at the top" % item)
        input("Press any key to continue...")

    elif ch == '4':
        display(s)
        input("Press any key to continue...")

    elif ch == '5':
        break

    else:
        print("Invalid choice! Please enter a number between 1 to 5.")
        input("Press any key to continue...")
