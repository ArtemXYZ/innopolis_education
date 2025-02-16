"""
     Модуль содержит варианты реализации стека.
"""



class Stack:
    """
        Класс-представление стека.

        * Пример использования:

            stack = Stack()

            stack.push(1)
            stack.push(2)
            stack.push(3)

            print(stack.peek())

            print(stack.pop())

            print(stack.size())

            print(stack.is_empty())

            print(stack.pop())
            print(stack.pop())
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("удаление из пустого стека")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("получение из пустого стека")

    def size(self):
        return len(self.items)

# --------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# --------------------------------------------------
class LinkedList:
    """
        * Пример использования:

            ll = LinkedList()
            ll.append(1)
            ll.append(2)
            ll.append(3)
            ll.prepend(0)
            ll.print_list()

            ll.delete_with_value(2)
            ll.print_list()
    """


    def __init__(self):
        self.head = None  # Начало списка

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# --------------------------------------------------
class Node_:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_:
    """
        # Пример использования

        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print(stack.peek())
        print(stack.pop())
        print(stack.pop())
    """
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("удаление из пустого стека")
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("получение из пустого стека")
        return self.top.data



# --------------------------------------------------

# class Node__:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
# class Stack__:
#     def __init__(self):
#         self.top = None
#
#     def is_empty(self):
#         return self.top is None
#
#     def push(self, data):
#         new_node = Node(data)
#         if self.top is None:
#             self.top = new_node
#         else:
#             new_node.prev = self.top
#             self.top.next = new_node
#             self.top = new_node
#
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("удаление из пустого стека")
#         popped_node = self.top
#         if self.top.prev is None:
#             self.top = None
#         else:
#             self.top = self.top.prev
#             self.top.next = None
#         return popped_node.data
#
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("получение из пустого стека")
#         return self.top.data
#
# # Пример использования
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.peek())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())













# -----------------------------------------
class CircularStack:
    """
        ///
    """

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
            self.top.next = self.top  # Указывает сам на себя, замыкая список
        else:
            new_node.next = self.top.next  # Новый узел указывает на первый узел
            self.top.next = new_node  # Последний узел (старый top) указывает на новый узел
            self.top = new_node  # Обновляем top

    def pop(self):
        if self.is_empty():
            raise IndexError("удаление из пустого стека")
        popped_node = self.top.next  # Первый узел (top.next) будет удален
        if self.top == self.top.next:
            # Если в списке только один элемент
            self.top = None
        else:
            self.top.next = popped_node.next  # Последний узел указывает на следующий после удаленного
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("получение из пустого стека")
        return self.top.next.data  # Возвращаем данные первого узла