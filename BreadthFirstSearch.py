
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            if s == 1:
                print("Arad", end=" | ")
            elif s == 2:
                print("Bucharest", end=" | ")
            elif s == 3:
                print("Craiova", end=" | ")
            elif s == 4:
                print("Dobreta", end=" | ")
            elif s == 5:
                print("Eforie", end=" | ")
            elif s == 6:
                print("Fagaras", end=" | ")
            elif s == 7:
                print("Giurgio", end=" | ")
            elif s == 8:
                print("Hirsova", end=" | ")
            elif s == 9:
                print("Iasi", end=" | ")
            elif s == 10:
                print("Lugoj", end=" | ")
            elif s == 11:
                print("Mehadia", end=" | ")
            elif s == 12:
                print("Neamt", end=" | ")
            elif s == 13:
                print("Oradea", end=" | ")
            elif s == 14:
                print("Pitest", end=" | ")
            elif s == 15:
                print("Rimnicu_Vilsea", end=" | ")
            elif s == 16:
                print("Sibiu", end=" | ")
            elif s == 17:
                print("Timisora", end=" | ")
            elif s == 18:
                print("Urziceni", end=" | ")
            elif s == 19:
                print("Vaslui", end=" | ")
            elif s == 20:
                print("Zerind", end=" | ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.addEdge(1, 16)
g.addEdge(1, 17)
g.addEdge(1, 20)

g.addEdge(2, 6)
g.addEdge(2, 7)
g.addEdge(2, 14)
g.addEdge(2, 18)

g.addEdge(3, 4)
g.addEdge(3, 14)
g.addEdge(3, 15)

g.addEdge(4, 3)
g.addEdge(4, 11)

g.addEdge(5, 8)

g.addEdge(6, 2)
g.addEdge(6, 16)

g.addEdge(7, 2)

g.addEdge(8, 5)
g.addEdge(8, 18)

g.addEdge(9, 12)
g.addEdge(9, 19)

g.addEdge(10, 11)
g.addEdge(10, 17)

g.addEdge(11, 4)
g.addEdge(11, 10)

g.addEdge(12, 9)

g.addEdge(13, 16)
g.addEdge(13, 20)

g.addEdge(14, 2)
g.addEdge(14, 3)
g.addEdge(14, 15)

g.addEdge(15, 3)
g.addEdge(15, 14)
g.addEdge(15, 16)

g.addEdge(16, 1)
g.addEdge(16, 6)
g.addEdge(16, 13)
g.addEdge(16, 15)

g.addEdge(17, 1)
g.addEdge(17, 10)

g.addEdge(18, 2)
g.addEdge(18, 8)
g.addEdge(18, 19)

g.addEdge(19, 9)
g.addEdge(19, 18)

g.addEdge(20, 1)
g.addEdge(20, 13)

print("Following is Breadth First Traversal"
      " (starting from vertex 1)")


def main():
    print(" 1 - Arad\n",
          "2 - Bucharest",
          "3 - Craiova\n",
          "4 - Dobreta\n",
          "5 - Eforie\n",
          "6 - Fagaras\n",
          "7 - Giurgio\n",
          "8 - Hirsova\n",
          "9 - Iasi\n",
          "10 -Lugoj\n",
          "11 - Mehadia\n",
          "12 - Neamt\n",
          "13 - Oradea\n",
          "14 - Pitesti\n",
          "15 - Rimnicu_Vilsea\n",
          "16 - Sibiu\n",
          "17 - Timisora\n",
          "18 - Urziceni\n",
          "19 - Vaslui\n",
          "20 - Zerind\n")
    op = int(input("Escolha o ponto de partida: "))
    g.BFS(op)


main()
