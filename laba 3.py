from abc import ABCMeta, abstractmethod


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, message: str) -> None:
        pass


class Observable(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.observers = []

    def register(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)


class feed(Observable):

    def add_news(self, news: str) -> None:
        self.notify_observers(news)


class feeder(Observer):

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print('{} событие: {}'.format(self.name, message))


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
        if self.i > len(self.visited) - 1:
            return None #raise StopIteration()
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

iter = GraphIterator(graph)
feed = feed()
feed.register(feeder('First'))
feed.register(feeder('Second'))
print('Проход:')

current = iter.current
while current != None:
    print(iter.current())
    if current == "B":
        feed.add_news('посещена вершина B')
    current = iter.__next__()

# for i in iter:
#     print(i)
#     if i == "B":
#         feed.add_news('посещена вершина B')
#     if i == "E":
#         feed.add_news('посещена вершина E')
