
class Node:
    """
       Класс Node представляет узел бинарного дерева.

       Atributes:
           value: значение узла
           left (Node): левый потомок узла
           right (Node): правый потомок узла
       """
    def __init__(self, value):
        """
        Инициализирует узел с заданным значением.
        """
        self.value = value
        self.left = None
        self.right = None


    def __str__(self):
        res = f'значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res


class BinaryTree:
    """
       Класс BinaryTree представляет бинарное дерево.

       Attributes:
             root_value - корневой узел бинарного дерева

       Methods:
           __init__(self) - Конструктор класса
           add(self, value) -  Добавление нового элемента
           search(self, value) - Метод внутреннего поиска
           count_elements(self) - Подсчитывает количество элементов в бинарном дереве
           delete(self, value) - Удаляет узел со значением value из бинарного дерева
           print_tree(self) - Функция вывода на экран бинарного дерева с отображением узлов
       """

    def __init__(self, root_value):
        self.root = Node(root_value)

    def add(self, value):
        """
        Добавляет новый элемент в бинарное дерево.

        Args:
        value: новый элемент для добавления
        """

        res = self.search(self.root, value)

        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print('Хорош')

    def search(self, node, value, parent=None):
        """
        Метод внутреннего поиска
        Поиск узла с value и его родительского элемента
        Поиск начинается с node

        Parameters:
            node: С какого узла начать поиск
            value: Значение для поиска
            parent(optional): Точки на текущем родительском узле, используемые для целей рекурсии
        """
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)


    def count_elements(self):
        """
        Подсчитывает количество элементов в бинарном дереве.
        """

        def count(node):
            if node is None:
                return 0
            return count(node.left) + count(node.right) + 1

        return count(self.root)

    def delete(self, value):
        """
        Удаляет узел со значением value из бинарного дерева.
        """
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        """"
        Вспомогательная функция для метода удаления

              Parameters:
                  value: Значение для удаления
                  node: Текущий узел
        """
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                min_value = self._find_min(node.right)
                node.value = min_value
                node.right = self._delete(node.right, min_value)

        return node

    def _find_min(self, node):
        """"
        Внутренняя функция, которая находит узел с минимальным значением в дереве, начиная с узла `node`.
        """
        while node.left is not None:
            node = node.left
        return node.value

    def print_tree(self):
        """
        Функция вывода на экран бинарного дерева с отображением узлов
        """
        self._print_tree(self.root, 0)

    def _print_tree(self, node, level):
        """"
        Вспомогательная функция для метода вывода на экран бинарного дерева с отображением узлов

        Parameters:
                level: Текущий уровень
                node: Текущий узел
        """
        if node is not None:
            self._print_tree(node.right, level + 1)
            print("    |" * level + "---", node.value)
            self._print_tree(node.left, level + 1)



bt = BinaryTree(5)
bt.add(10)
bt.add(15)
bt.add(3)
bt.add(4)
bt.add(45)
bt.add(2)
bt.add(1)

#print(bt.root)
#print(bt.search(bt.root, 8)[1])
#print(bt.root.left)
#print(bt.root.right)
#print(bt.count_elements())

bt.print_tree()
bt.delete(1)
bt.delete(15)
print('--------------------------------------------------------------------------')
bt.print_tree()