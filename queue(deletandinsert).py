queue = []  # Initialize an empty list to serve as the queue

def enqueue():
    n = int(input("Enter the element to be inserted into the queue: "))
    queue.append(n)

def dequeue():
    if len(queue) == 0:
        print("QUEUE IS EMPTY")
        print(".......")
    else:
        print(queue[0], "is the element deleted from the queue")
        del queue[0]
        print("....")

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Elements of the queue are:")
        for element in queue:
            print(element, end=" ")

        print("\nFront of the queue is", queue[0])
        print("Rear of the queue is", queue[-1])
        print()

while True:
    print("Enter the option from below: \n1- Enqueue operation \n2- Dequeue operation \n3- Display \n4- Exit")
    option = int(input())

    if option == 1:
        print("Enqueue operation")
        enqueue()

    elif option == 2:
        print("Dequeue operation")
        dequeue()

    elif option == 3:
        print("Display")
        display()

    elif option == 4:
        break
    else:
        print("Invalid option. Please enter a valid option.")
