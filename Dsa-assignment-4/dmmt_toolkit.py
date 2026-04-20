# ---------------- BST ----------------

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def insert(self, root, val):
        if root is None:
            return Node(val)

        if val < root.data:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def search(self, root, val):
        if root is None:
            return False

        if root.data == val:
            return True

        if val < root.data:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def delete(self, root, val):
        if root is None:
            return root

        if val < root.data:
            root.left = self.delete(root.left, val)

        elif val > root.data:
            root.right = self.delete(root.right, val)

        else:
            # no child
            if root.left is None and root.right is None:
                return None

            # one child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # two children
            temp = root.right
            while temp.left:
                temp = temp.left

            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


# ---------------- GRAPH ----------------

class Graph:
    def __init__(self):
        self.g = {}

    def add_edge(self, u, v, w):
        if u not in self.g:
            self.g[u] = []

        self.g[u].append((v, w))

    def show(self):
        for i in self.g:
            print(i, "->", self.g[i])

    def bfs(self, start):
        visited = []
        queue = [start]

        print("BFS:", end=" ")

        while queue:
            node = queue.pop(0)

            if node not in visited:
                print(node, end=" ")
                visited.append(node)

                for nbr, _ in self.g.get(node, []):
                    queue.append(nbr)

    def dfs(self, node, visited=None):
        if visited is None:
            visited = []

        print(node, end=" ")
        visited.append(node)

        for nbr, _ in self.g.get(node, []):
            if nbr not in visited:
                self.dfs(nbr, visited)


# ---------------- HASH TABLE ----------------

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_fun(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self.hash_fun(key)
        self.table[idx].append((key, value))

    def get(self, key):
        idx = self.hash_fun(key)

        for k, v in self.table[idx]:
            if k == key:
                return v

        return None

    def delete(self, key):
        idx = self.hash_fun(key)

        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                self.table[idx].pop(i)
                return True

        return False

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# ---------------- MAIN ----------------

def main():
    print("BST PART")

    b = BST()
    root = None

    arr = [50, 30, 70, 20, 40, 60, 80]

    for i in arr:
        root = b.insert(root, i)

    print("Search 20:", b.search(root, 20))
    print("Search 90:", b.search(root, 90))

    print("Inorder:", end=" ")
    b.inorder(root)
    print()

    root = b.delete(root, 20)
    print("After delete 20:", end=" ")
    b.inorder(root)
    print()

    root = b.insert(root, 65)
    root = b.delete(root, 60)
    print("After delete 60:", end=" ")
    b.inorder(root)
    print()

    root = b.delete(root, 50)
    print("After delete 50:", end=" ")
    b.inorder(root)
    print()

    print("\nGRAPH PART")

    g = Graph()

    edges = [
        ("A","B",2), ("A","C",4), ("B","D",7),
        ("B","E",3), ("C","E",1), ("D","F",5),
        ("E","D",2), ("E","F",6), ("C","F",8)
    ]

    for u,v,w in edges:
        g.add_edge(u,v,w)

    g.show()

    g.bfs("A")

    print("\nDFS:", end=" ")
    g.dfs("A")

    print("\n\nHASH TABLE PART")

    h = HashTable(5)

    keys = [10,15,20,7,12]

    for k in keys:
        h.insert(k, k*10)

    h.display()

    print("Get 10:", h.get(10))
    print("Get 15:", h.get(15))
    print("Get 7:", h.get(7))

    h.delete(15)
    print("After delete 15:")
    h.display()


main()