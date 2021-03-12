import random


class Graph(object):
    def __init__(self, currentPattern):
        self.nodes = {}
        self.currentPattern = currentPattern
        self.nodes[currentPattern] = Edge()

    def addUpdateEdge(self, newPattern):
        try:
            self.nodes[newPattern]
            self.nodes[self.currentPattern].addEdge(newPattern)
        except:
            self.nodes[newPattern] = Edge()
            self.nodes[self.currentPattern].addEdge(newPattern)
        self.currentPattern = newPattern

    def randomNode(self):
        edges = self.nodes[self.currentPattern]
        return edges.randomNum()


class Edge(object):
    def __init__(self):
        self.connections = {}
        self.size = 0

    def addEdge(self, newPattern):
        if newPattern in self.connections:
            self.connections[newPattern] = self.connections[newPattern] + 1
        else:
            self.size += 1
            self.connections[newPattern] = 1

    def edgeSize(self):
        return self.size

    def randomNum(self):
        num = random.uniform(0, sum(self.connections.values()))

        total = 0

        for key, freq in self.connections.items():
            total += freq
            if num < total:
                return key
        return key
