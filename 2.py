class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Добавить узел в конец списка
    def add_in_tail(self, item):
        new_node = Node(item)  # Создаем новый узел
        if self.head is None:  # Если список пуст
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Устанавливаем ссылку на новый узел
            self.tail = new_node  # Обновляем tail


    # Вывести на экран все узлы
    def print_all_nodes(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()

    # Найти узел по значению (первое совпадение)
    def find(self, val):
        current = self.head
        while current is not None:
            if current.value == val:
                return current
            current = current.next
        return None

    # Найти все узлы с переданным значением
    def find_all(self, val):
        result = []
        current = self.head
        while current is not None:
            if current.value == val:
                result.append(current)
            current = current.next
        return result

        # Удалить узел с переданным значением.
        # Если all=False, то учитывается первое совпадение. Иначе удаляются все узлы с данным значением.
    def delete(self, val, all=False):
        current = self.head
        previous = None
        while current is not None:
            if current.value == val:
                if previous is None:
                    self.head = current.next
                    if self.head is None:
                        self.tail = None
                else:
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                if not all:
                    break
            else:
                previous = current
            current = current.next

  # Очистить весь список
    def clean(self):
        self.head = None
        self.tail = None
# Вернуть количество узлов в списке
    def len(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
# Вставить узел после указанного
    def insert(self, afterNode, newNode):
        if afterNode is None:
            return
        newNode.next = afterNode.next
        afterNode.next = newNode
        if afterNode == self.tail:
            self.tail = newNode


 # Вернуть количество узлов в списке
    def len(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

            # Вставить узел после указанного
    def insert(self, afterNode, newNode):
        if afterNode is None:
            return
        newNode.next = afterNode.next
        afterNode.next = newNode
        if afterNode == self.tail:
            self.tail = newNode
linked_list = LinkedList()
linked_list.add_in_tail(1)
linked_list.add_in_tail(2)
linked_list.add_in_tail(3)
linked_list.add_in_tail(4)

print("Список:")
linked_list.print_all_nodes()

print("Количество узлов:", linked_list.len())

print("Найти узел со значением 3:", linked_list.find(3).value)

print("Найти все узлы со значением 2:")
for node in linked_list.find_all(2):
    print(node.value)  # Вывод: 2

linked_list.delete(2, all=True)

print("Список после удаления:")
linked_list.print_all_nodes()

linked_list.insert(linked_list.find(3), Node(5))

print("Список после вставки:")
linked_list.print_all_nodes()

linked_list.clean()

print("Список после очистки:")
linked_list.print_all_nodes()











