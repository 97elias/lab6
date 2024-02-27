# DD1321
# Uppgift, Lab3: Binära träd 
# Författare: Elias Albag och Joakim Ergon
# Datum: 31-01-2024

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)
    
    def __lt__(self,other):
        return self < other

class Bintree:
    def __init__(self):
        self.root = None

    def store(self, key):
        # Sorterar in key i trädet
        self.root = recstore(self.root, key) 

    def __contains__(self, key):
        # True om key finns i trädet, False annars
        return recsearch(self.root, key)

    def write(self):
        # Skriver ut trädet i inorder
        recwrite(self.root)
        print("\n")

def recstore(root, key):
    # Sorterar in key i trädet
    if root is None: # Basfall
        return Node(key)
    else: # Rekursivt fall
        if key < root.value:
            root.left = recstore(root.left, key)
        else:
            root.right = recstore(root.right, key)
    return root

def recsearch(root, key):
    if root is None: # Basfall
        return False
    elif root.value == key:
        return True
    else: # Reskursivt fall 
        if key < root.value:
            return recsearch(root.left, key)
        else:
            return recsearch(root.right, key)


def recwrite(root):
    # Skriver ut trädet i inorder
    if root is not None: 
        recwrite(root.left) 
        print(root.value)
        recwrite(root.right)
