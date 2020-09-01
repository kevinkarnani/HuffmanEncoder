class tree:
    def __init__(self, left, right, parent) :
        self.left = left
        self.right = right
        self.parent = parent
    
    def __str__(self):
        return "Parent: " + str(self.parent) + ", Left: " + str(self.left) + ", Right: " + str(self.right) 

class alphabet:
    def __init__(self, symb, prob, leaf):
        self.symb = symb
        self.prob = prob
        self.leaf = leaf

    def __str__(self) :
        return "Symbol: " + str(self.symb) + ", Probability: " + str(self.prob) + ", Leaf: " + str(self.leaf)

class forest:
    def __init__(self, weight, root):
        self.weight = weight
        self.root = root

    def __str__(self):
        return "Weight: " + str(self.weight) + ", Root: " + str(self.root)
    
def lightones(least, second):
    if FOREST[0].weight <= FOREST[1].weight:
        least = 0
        second = 1
    else:
        least = 1
        second = 0
    for i in range(2, len(FOREST)):
        if FOREST[i].weight < FOREST[least].weight:
            second = least
            least = i
        elif FOREST[i].weight < FOREST[second].weight:
            second = i
    return (least,second)
    
def create(lefttree, righttree):
    lastnode = len(TREE)
    
    TREE.append(tree(None, None, None))
    TREE[lastnode].left = FOREST[lefttree].root
    TREE[lastnode].right = FOREST[righttree].root
    
    TREE[lastnode].parent = None
    TREE[FOREST[lefttree].root].parent = lastnode
    TREE[FOREST[righttree].root].parent = lastnode
    return lastnode

def Huffman():
    i, j = 0, 0
    last = len(FOREST)
    while last > 1:
        i, j = lightones(i, j)
        new = create(i, j)
        FOREST[i].weight = FOREST[i].weight + FOREST[j].weight
        FOREST[i].root = new
        FOREST[j] = FOREST[last-1]
        del FOREST[last-1]
        last -= 1

def walk(letter):
    code = ''
    index = letter.leaf
    parent = list(filter(lambda x: x.left == index or x.right == index, TREE))
    if len(parent) > 1:
        print("two roots?? bad algorithm")
        return
    parent = parent[0]
    if parent.left == index:
        node = parent.left
    else:
        node = parent.right
    grandparent = parent.parent
    while grandparent != None:
        if parent.left == node:
            code += '0'
        else:
            code += '1'
        node = TREE[node].parent
        parent = TREE[grandparent]
        grandparent = parent.parent
    if parent.left == node:
        code += '0'
    else:
        code += '1'
    return code[::-1]

TREE = []
ALPHABET = []
FOREST = []

if __name__ == "__main__":
    print("Welcome to Huffman Encoder!")
    total = 0
    inputs = {}
    while True:
        letter = input("Add a Letter: ")
        frequency = int(input("Frequency of Letter: "))
        if not letter in inputs:
            inputs[letter] = frequency
        else:
            print(f"Letter '{letter}' already added.")
            continue
        total += frequency
        add = input("Add another letter? (y/n)\n")
        if (add == "y"):
            continue
        elif (add == "n"):
            print("Okay, lets start!")
            break
        else:
            print("Unrecognized input.")
            continue
    for index, letter in enumerate(inputs):
        TREE.append(tree(None, None, None))
        ALPHABET.append(alphabet(letter, inputs[letter] / total, index))
        FOREST.append(forest(inputs[letter] / total, index))
    Huffman()
    for k in range(0, len(TREE)):
        print(TREE[k])
    for alphabet in ALPHABET:
        print(alphabet.symb, ":", walk(alphabet))
