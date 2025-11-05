# lab assignment 5
# Create Student Record System using Singly Linked List.

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        if not temp:
            print("No records found.")
            return
        while temp:
            print(f"Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next

# Main Program
ll = LinkedList()
ll.add_student(1, "Riya", 89)
ll.add_student(2, "Amit", 76)
ll.add_student(3, "Sneha", 92)
print("\nStudent Records:")
ll.display()
