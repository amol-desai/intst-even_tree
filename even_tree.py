class Node(object):
    def __init__(self,id):
        self.id = id
        self.parent = self
        self.children = []
        self.isLeaf = True
        self.isRoot = False

    def add_child(self, obj):
        self.children.append(obj)

    def unset_leaf(self):
        self.isLeaf = False

    def set_root(self):
        self.isRoot = True

##S = raw_input()
##N = map(int,S.split())
##num_nodes = N.pop(0)
##num_edges = N.pop(0)

N = map(int,raw_input().split())
num_nodes = N.pop(0)
num_edges = N.pop(0)
x = []
for i in range(1,num_edges+1):
    x = (map(int,raw_input().split()))
    N.append(x[0])
    N.append(x[1])

nodes = []
for i in range(1, num_nodes+1):
    nodes.append(Node(i))

for i in range(0,len(N),2):
    nodes[N[i]-1].parent = (nodes[N[i+1]-1])
    nodes[N[i+1]-1].add_child(nodes[N[i]-1])
    nodes[N[i+1]-1].unset_leaf()
nodes[0].set_root()        

def print_tree():
    for node in nodes:
        print node.id
        print node.parent.id
        print node.children
        print node.isLeaf
        print node.isRoot
        print "*******************"

count = 0
def snip():
    global count
    for node in nodes:
        if node.isLeaf:
            while ((len(node.parent.children) > 1) & (node.parent.isRoot == False)):
                node = node.parent
            if node.parent.isRoot == False:
                node.parent.parent.children.remove(node.parent)
                if(len(node.parent.parent.children) == 0):
                    node.parent.parent.isLeaf = True
                node.parent.parent = node.parent
                node.parent.set_root()
                count = count + 1

old_count = 0      
snip()
while count != old_count:
    old_count = count
    snip()

print count
