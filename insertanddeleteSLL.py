class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node_at_position(self, position):
        if not self.head:
            print("List is empty. Deletion not possible.")
            return

        if position == 0:
            temp = self.head
            self.head = temp.next
            temp = None
            return

        current_node = self.head
        for i in range(position - 1):
            if current_node is None:
                print("Invalid position. Deletion not possible.")
                return
            current_node = current_node.next

        if current_node is None or current_node.next is None:
            print("Invalid position. Deletion not possible.")
            return

        node_to_delete = current_node.next
        current_node.next = node_to_delete.next
        node_to_delete = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()

    # Appending nodes to the linked list
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    print("Original linked list:")
    linked_list.display()

    position = int(input("Enter the position to delete: "))
    linked_list.delete_node_at_position(position)

    print("Linked list after deletion:")
    linked_list.display()
