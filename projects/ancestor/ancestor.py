
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
   
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            path = s.pop()
            last_vertex = path[-1]
            if last_vertex in visited:
                continue
            else:
                visited.add(last_vertex)
            for neighbor in self.get_neighbors(last_vertex):
                next_path = path[:]
                next_path.append(neighbor)
                if neighbor == destination_vertex:
                    return next_path
                else:
                    s.push(next_path)



def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for vertex_1, vertex_2 in ancestors:
        graph.add_vertex(vertex_1)
        graph.add_vertex(vertex_2)

    for vertex_1, vertex_2 in ancestors:
        graph.add_edge(vertex_1, vertex_2)

    target_vertex = None

    longest_path = 1

    for vertex in graph.vertices:
        path = graph.dfs(vertex, starting_node)
        if path:
            print(path)
            if len(path) > longest_path:
                longest_path = len(path)
                target_vertex = vertex
        elif not path and longest_path == 1:
            target_vertex = -1

    return target_vertex