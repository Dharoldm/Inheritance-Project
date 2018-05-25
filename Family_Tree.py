from Person import Person
from Graph import Graph

class FamilyTree(object):

    def __init__(self, house, head=None):
        self.house = house
        self.tree = Graph()
        if head:
            self.tree.adj_map[head.name] = head
            self.tree.size +=1

    def __repr__(self):
        for i in self.tree.adj_map:
            return i

    def members(self):
        return self.tree.vertex_count()

Eric = Person("Eric", 198, "male")
Tree = FamilyTree("Hawick", Eric)
print(Tree.members())
print(Tree)