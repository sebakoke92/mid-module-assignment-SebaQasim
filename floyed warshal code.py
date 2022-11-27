# Python program solve all pair shortest paths using the Floyd Warshall algorithm.
import datetime
start_time = datetime.datetime.now()
# Number of nodes in the graph.
n = 4
# INF is the large value used for the distance between nodes with no common path.
import sys

INF = sys.maxsize

# printing solution function


def printSolution(dist):
    print(
        "The solution  matrix represent the shortest distances between every pair of nodes"
    )
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("%5s\t" % ("INF"), end=" ")
            else:
                print("%5d\t" % (dist[i][j]), end=" ")
            if j == n - 1:

                print()

    """floydWarshall algorithm input will be a matrix
    called graph represent the distances
     between nodes in graphs"""

    """ floydWarshall algorithm output will be a matrix 
     have the shortest distances
     between every pair of nodes in graphs """


def floydWarshall(graph):
    dist = graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    printSolution(dist)


# Driver's code
if __name__ == "__main__":
    """
               8
         (0)------->(3)
          |         /|\
       7  |          |
          |          | 2
         \|/         |
         (1)------->(2)
               5           """

    graph = [[0, 7, INF, 8], [INF, 0, 5, INF], [INF, INF, 0, 2], [INF, INF, INF, 0]]
    #  call Floyd Warshall function
    floydWarshall(graph)

 

end_time = datetime.datetime.now()
print(end_time - start_time)
    # rptree.py
# Snip...

class DirectoryTree:
    def __init__(self, root_dir):
        self._generator = TreeGenerator(root_dir)

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)