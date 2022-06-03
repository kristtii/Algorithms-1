class node:
    def __init__(self, index):
        self.value = index
        self.next = None

    def get_last_node_in_chain(self):
        last = self

        while(last.next != None):
            last = last.next

        return last

class graph:
    def __init__(self, size, file):
        self.size = size
        self.nodes = [node(i) for i in range(size)]

        for f in file.readlines():
            line = f.split(' ')
            self.addEdge(int(line[0]), int(line[1]))
            self.addEdge(int(line[1]), int(line[0]))


    def addEdge(self, index, newnode):
        last = self.nodes[index].get_last_node_in_chain()
        last.next = newnode



