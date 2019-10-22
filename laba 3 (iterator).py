# Создать граф
# Сделать итератор для перечисления узлов графа

# Поиск в глубину или в ширину. Найти нужные и добавить в наблюдателя.

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


class GraphIterator:
    def __init__(self, graph, start='A'):
        self.graph = graph
        self.start = start
        self.next = self.start
        self.visited = []
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.next not in self.visited:
            self.visited.append(self.next)
            for n in graph[self.next]:
                dfs(graph, n, self.visited)
        if self.i > len(self.visited)-1:
            raise StopIteration()
        self.next = self.visited[self.i]
        return self.next

    def current(self):
        return self.next

    def first(self):
        self.next = self.start
        self.i = 0


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
print(graph)
iter = GraphIterator(graph)
print(dfs(graph, 'A', []))
# print('Первый обход:')
# for i in iter:
#     print(i)
# print(iter.current())
# iter.first()
# print(iter.current())
# print('Второй обход:')
# for i in iter:
#     print(i)
