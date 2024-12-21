class Node:

    def __init__(self, value):
        self.value = value  # sõlme väärtus
        self.left = None    # vasak laps
        self.right = None   # parem laps


class BinaryTree: # Kasutab kahendpuu struktuuri
    def __init__(self):
        self.root = None  

    def insert(self, value): # Kui puul pole veel juurt, siis alustab juure lisamisega
        if self.root is None:# Alustab juurest
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        """
        Helper method to insert a value recursively.
        """
        if value < current.value:
            if current.left is None: # Kui väärtus on väiksem, siis liigu vasakule
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else: # kui väärtus  on suurem või võrdne, liigu paremale
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def in_order_traversal(self): # järjestab sisestatud sõlmed suuruse järgi
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, current, result):
        if current is not None:
            self._in_order_recursive(current.left, result) # Liigu kõigepealt vasakpoolset haru mööda
            result.append(current.value)
            self._in_order_recursive(current.right, result) #  siis mööda parempoolset haru


#Näide
if __name__ == "__main__":
    tree = BinaryTree()
    values = [7, 3, 10, 1, 5, 8, 12, 66,15,25,97,46,24]  # näidisandmestik

    for value in values:
        tree.insert(value)

    # Perform in-order traversal and print the result
    print("sisestatud tulemused järjekorras:", tree.in_order_traversal())
