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

#S = raw_input()
#N = map(int,S.split())
#num_nodes = N.pop(0)
#num_edges = N.pop(0)

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

def sub_tree_size(node):
#    print "sub_tree_size:",node.id
    global size
##    if node.isLeaf:
##        pass
##    else:
    for child in node.children:
        size = sub_tree_size(child) + 1
#    print "size =",size
#    print "exit sub_tree_size:",node.id
    return size

def snip(node):
#    print "snip:",node.id
    global count
    global size
    size = 1
    if node.isRoot:
        pass
    elif ((len(node.children)%2 != 0) & (sub_tree_size(node)%2 == 0)):
#        print "cutting ", node.id, " from ",node.parent.id
        node.parent.children.remove(node)
        if(len(node.parent.children)==0):
            node.parent.isLeaf = True
        node.parent = node
        node.set_root()
        count = count + 1
    else:
        snip(node.parent)
#    print "exit snip:",node.id

def dfs(node):
#    print "dfs:",node.id
    for child in node.children:
        #print "I am on child ",child.id
        if not child.isLeaf:
         #   print "child ",child.id," is not a leaf..looking at child"
            dfs(child)
        #print "child is leaf...should go to next child"
    snip(node)
#    print "exit dfs:",node.id

count = 0
old_count = 0
dfs(nodes[0])
while count != old_count:
    old_count = count
    for node in nodes:
        if node.isRoot:
            dfs(node)

print count
