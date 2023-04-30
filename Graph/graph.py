import polska
from typing import Tuple, List
class EmptyGraphError(Exception):
    pass

class Vertex:
    def __init__(self, key: str) -> None:
        self.key = key

    def __eq__(self, other) -> bool:
        return self.key == other.key
    
    def __hash__(self):
        return hash(self.key)

class Edge:
    def __init__(self, key) -> None:
        self.key = key
    
    def __eq__(self, other) -> bool:
        return self.key == other.key
    
    def __hash__(self):
        return hash(self.key)

class GraphMatrix:
    def __init__(self, init_val=0) -> None:
        self.vertices = {}
        self.list = {}
        self.matrix = []
        self.init_val = init_val

    def insertVertex(self, vertex) -> None:
        if self.isEmpty():
            self.matrix.append([self.init_val])
            self.vertices[vertex.key] = 0
            return
        for i, item in enumerate(self.matrix):
            self.matrix[i].append(0)
        self.matrix.append([self.init_val for _ in range(len(self.matrix)+1)])
        self.vertices[vertex.key] = len(self.matrix) - 1

    def insertEdge(self, vertex1, vertex2, edge) -> None:
        if self.isEmpty():
            raise EmptyGraphError
        self.list[edge.key] = vertex1.key,vertex2.key
        vertex1_idx = self.vertices[vertex1.key]
        vertex2_idx = self.vertices[vertex2.key]
        self.matrix[vertex1_idx][vertex2_idx] += 1
        self.matrix[vertex2_idx][vertex1_idx] += 1

    def deleteVertex(self, vertex) -> None:
        idx = self.vertices[vertex.key]
        if idx == 0:
            del self.vertices[vertex.key]
            for keys in self.vertices:
                self.vertices[keys] -= 1
            self.matrix.pop(idx)
            for i, item in enumerate(self.matrix):
                self.matrix[i].pop(idx)
            l = []
            for keys, valuse in self.list.items():
                if vertex.key in valuse:
                    l.append(keys)
            for i in l:
                del self.list[i]
            return
        
        if idx == len(self.vertices) - 1:
            del self.vertices[vertex.key]
            self.matrix.pop(idx)
            for i, item in enumerate(self.matrix):
                self.matrix[i].pop(idx)
            l = []
            for keys, valuse in self.list.items():
                if vertex.key in valuse:
                    l.append(keys)
            for i in l:
                del self.list[i]
            return
        
        self.matrix.pop(idx)
        for i, item in enumerate(self.matrix):
            for j in range(idx, len(self.matrix[i])-1):
                self.matrix[i][j] = self.matrix[i][j+1]
            self.matrix[i].pop(len(self.matrix[i])-1)

        l = []
        for keys, valuse in self.list.items():
                if vertex.key in valuse:
                    l.append(keys)
        for i in l:
                del self.list[i]
        del self.vertices[vertex.key]
        for keys in self.vertices:
            if self.vertices[keys] > idx:
                self.vertices[keys] -= 1

        

    def deleteEdge(self, vertex1, vertex2) -> None:
        for keys, values in self.list.items():
            if vertex1.key == values[0] and vertex2.key == values[1]:
                del self.list[keys]
                vertex1_idx = self.vertices[vertex1.key]
                vertex2_idx = self.vertices[vertex2.key]
                self.matrix[vertex1_idx][vertex2_idx] -= 1
                self.matrix[vertex2_idx][vertex1_idx] -= 1
                return

    def getVertexIdx(self, vertex) -> int:
        return self.vertices[vertex.key]
    
    def getVertex(self, vertex_idx) -> int:
        for keys, values in self.vertices.items():
            if values == vertex_idx:
                return keys

    def neighboursIdx(self, edge) -> int:
        return self.vertices[self.list[edge.key][0]], self.vertices[self.list[edge.key][1]]
    
    def neighbours(self, edge_idx) -> Tuple[str,str]:
        return self.list[edge_idx]

    def isEmpty(self) -> bool:
        return not bool(self.vertices)
    
    def edges(self) -> List[Tuple[str,str]]:
        return [value for  value in self.list.values()]

    def order(self) -> int:
        return len(self.vertices)

    def size(self) -> int:
        return len(self.list)
    
class GraphList:
    def __init__(self, init_val=0) -> None:
        self.vertices = {}
        self.neig_list = {}
        self.list = []
        self.init_val = init_val

    def insertVertex(self, vertex) -> None:
        if self.isEmpty():
            self.vertices[vertex.key] = 0
            self.list.append([])
            return
        self.vertices[vertex.key] = len(self.vertices)
        self.list.append([])

    def insertEdge(self, vertex1, vertex2, edge) -> None:
        if self.isEmpty():
            raise EmptyGraphError
        self.neig_list[edge.key] = vertex1.key,vertex2.key
        vertex1_idx = self.vertices[vertex1.key]
        vertex2_idx = self.vertices[vertex2.key]
        self.list[vertex1_idx].append(vertex2_idx)
        self.list[vertex2_idx].append(vertex1_idx)
    
    def deleteVertex(self, vertex) -> None:
        idx = self.vertices[vertex.key]
        if idx == 0:
            del self.vertices[vertex.key]
            for keys in self.vertices:
                self.vertices[keys] -= 1
            self.list.pop(idx)
            for i, item in enumerate(self.list):
                self.list[i].pop(idx)
                self.list[i] = [j-1 for j in self.list[i]]
            l = []
            for keys, valuse in self.neig_list.items():
                if vertex.key in valuse:
                    l.append(keys)
            for i in l:
                del self.neig_list[i]
            return
        
        if idx == len(self.vertices) - 1:
            del self.vertices[vertex.key]
            self.list.pop(idx)
            for i, item in enumerate(self.list):
                for j, item in enumerate(self.list[i]):
                    if self.list[i][j] == idx:
                        self.list[i].pop(j)
            l = []
            for keys, valuse in self.neig_list.items():
                if vertex.key in valuse:
                    l.append(keys)
            for i in l:
                del self.neig_list[i]
            return
        
        self.list.pop(idx)
        for i, item in enumerate(self.list):
            poped = False
            mem = None
            for j, item in enumerate(self.list[i]):
                if self.list[i][j] == idx and not(poped):
                    mem = j
                if self.list[i][j] > idx:
                    self.list[i][j] -= 1
            if mem is not None:
                self.list[i].pop(mem)
        l = []
        for keys, valuse in self.neig_list.items():
                if vertex.key in valuse:
                    l.append(keys)
        for i in l:
                del self.neig_list[i]
        del self.vertices[vertex.key]
        for keys in self.vertices:
            if self.vertices[keys] > idx:
                self.vertices[keys] -= 1
        

    def deleteEdge(self, vertex1, vertex2) -> None:
        for keys, values in self.neig_list.items():
            if vertex1.key == values[0] and vertex2.key == values[1]:
                del self.neig_list[keys]
                vertex1_idx = self.vertices[vertex1.key]
                vertex2_idx = self.vertices[vertex2.key]
                for i, item in enumerate(self.list):
                    if i == vertex1_idx:
                        self.list[i].remove(vertex2_idx)
                    if i == vertex2_idx:
                        self.list[i].remove(vertex1_idx)
                return

    def getVertexIdx(self, vertex) -> int:
        return self.vertices[vertex.key]
    
    def getVertex(self, vertex_idx) -> int:
        for keys, values in self.vertices.items():
            if values == vertex_idx:
                return keys

    def neighboursIdx(self, edge) -> Tuple[int,int]:
        return self.vertices[self.neig_list[edge.key][0]], self.vertices[self.neig_list[edge.key][1]]
    
    def neighbours(self, edge_idx) -> Tuple[int,int]:
        return self.neig_list[edge_idx]

    def isEmpty(self) -> bool:
        return not bool(self.vertices)
    
    def edges(self) -> List[Tuple[str,str]]:
        return [value for  value in self.neig_list.values()]

    def order(self) -> int:
        return len(self.vertices)

    def size(self) -> int:
        return len(self.neig_list)

vertices = [Vertex(i[2]) for i in polska.polska]
edges =  polska.graf

gm = GraphMatrix()
gl = GraphList()
i = 0
for vertex in vertices:
    gm.insertVertex(vertex)
    gl.insertVertex(vertex)
for edge in edges:
    gm.insertEdge(Vertex(str(edge[0])), Vertex(str(edge[1])), Edge(str(i)))
    gl.insertEdge(Vertex(str(edge[0])), Vertex(str(edge[1])), Edge(str(i)))
    i+=1

gm.deleteVertex(Vertex('K'))
gm.deleteEdge(Vertex('W'), Vertex('E'))
gm.deleteEdge(Vertex('E'), Vertex('W'))

gl.deleteVertex(Vertex('K'))
gl.deleteEdge(Vertex('W'), Vertex('E'))
gl.deleteEdge(Vertex('E'), Vertex('W'))

polska.draw_map(gm.edges())  
#polska.draw_map(gl.edges()) 
