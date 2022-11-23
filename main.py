
class TreeStore:

    def __init__(self, items_list):

        self.items = items_list

    def get_all(self):
        """
        Возвращает изначальный массив элементов
        """
        return self.items

    def get_item(self, id_item):
        """
        Принимает id элемента и возвращает сам объект элемента
        """
        for i in self.items:
            if i["id"] == id_item:
                return i

    def get_children(self, id_item):
        """
        Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,
        чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив
        """
        children_list = []
        for i in self.items:
            if i["parent"] == id_item:
                children_list.append(i)
        return children_list

    def get_parent(self, id_item):
        parent = []
        for i in self.items:
            if i["id"] == id_item:
                for x in self.items:
                    if x["id"] == i["parent"]:
                        parent.append(x)
        return parent

    def get_all_parents(self, id_item):
        """
        Принимает id элемента и возвращает массив из цепочки родительских элементов,
        начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,
        т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!
        """
        tree = self.get_parent(id_item)
        for el in tree:
            for i in self.items:
                if el["parent"] == i["id"]:
                    tree.append(i)
        return tree


if __name__ == '__main__':

    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]

    ts = TreeStore(items)



