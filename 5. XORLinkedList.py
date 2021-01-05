# get_pointer and dereference_pointer are considered as two pre-defined methods.

class Node:
    def __init__(self, val):
        self.val = val
        self.both = 0

class XORLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

    def add(self, element):
        newNode = Node(element)
        if self.head.val == None:
            self.head = self.tail = newNode
        else:
            newNode.both = get_pointer(self.tail)
            self.tail.both = self.tail.both ^ get_pointer(newNode)
            self.tail = newNode

    def get(self, ind):
        previousAddr = 0
        current = self.head
        for i in range(0,ind-1):
            temp = get_pointer(current)
            current = dereference_pointer(previousAddr^current.both)
            previousAddr = temp
            if curret.both == previousAddr and i < ind-2:
                print("Invalid index.")
                return None
        return current.val


if __name__ == "__main__":
    XORLinkedList = XORLinkedList()

    while True:
        choice = int(input("Chose the option: \n 1. ADD\t2. GET\t3. EXIT\n").strip())
        if choice == 1:
            element = int(input("Enter the element: "))
            XORLinkedList.add(element)
        elif choice == 2:
            ind = int(input("Enter the index: "))
            node = XORLinkedList.get(ind)
            if node != None:
                print(node)
        elif choice == 3:
            break
        else:
            print("Invalid choice.")
