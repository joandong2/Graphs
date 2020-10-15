"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Error vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty Queue and add starting vertex to it
        # This will keep track of all next_to_visit_vertices
        queue = []
        queue.append(starting_vertex)
        # Create an empty set to keep track of visited vertices
        visited = set()
        # While the queue is not empty
        while len(queue) > 0:
            # dequeue a vertex off the queue
            current_vertex = queue.pop(0)

            # if vertex not in visited vertices
            if current_vertex not in visited:
                # Print it
                print(current_vertex)
                # Add the vertex to our visited set
                visited.add(current_vertex)
                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = []
        stack.append(starting_vertex)
        visited = set()

        while len(stack) > 0:
            current_vertex = stack.pop()

            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()

        # see if the current node has been visited
        print(starting_vertex)
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and Add a PATH TO starting vertex
        # I.e add array [1] to the queue
        queue = [[starting_vertex]]

        # create visited set (its empty for now)
        visited = set()
        # while queue is not empty:
        while len(queue) > 0:
            # pop the list inside the queue, which is our path
            path = queue.pop(0)
            # print('path', path)
            # get the current vertex to analyze from the path and use the vertex at the END of the path array
            vertex = path[-1]

            # END CASE: check if the current vertex is same with our end vertex
            if vertex == destination_vertex:
                return path

            # check if vertex is already in visited
            elif vertex not in visited:
                # if not, get its neighbor, append in our queue
                for neighbor in self.get_neighbors(vertex):
                    # get the path from 103, then create a new list
                    new_path = list(path)
                    # append the neightbors to the new list
                    new_path.append(neighbor)
                    # append the new list to the queue
                    queue.append(new_path)

                # add the vertex in visisted set
                visited.add(vertex)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and Add a PATH TO starting vertex
        # I.e add array [1] to the stack
        stack = [[starting_vertex]]

        visited = set()
        while len(stack) > 0:
            path = stack.pop()
            vertex = path[-1]

            if vertex == destination_vertex:
                return path

            elif vertex not in visited:
                for neighbor in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)

                visited.add(vertex)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = [starting_vertex]

        print(starting_vertex)
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == destination_vertex:
                    return new_path

                dfs_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, new_path)
                if dfs_path is not None:
                    return dfs_path

        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
