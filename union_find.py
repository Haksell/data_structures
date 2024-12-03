from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.__len = n
        self.__parents = list(range(n))
        self.__ranks = [1] * n

    def __len__(self):
        return self.__len

    def __repr__(self):
        components = (
            str(list(self.components()))
            .replace(",", "")
            .replace("[", "{")
            .replace("]", "}")
        )[1:-1]
        return f"{self.__class__.__name__}({components})"

    def find(self, u):
        while u != self.__parents[u]:
            self.__parents[u] = self.__parents[self.__parents[u]]
            u = self.__parents[u]
        return u

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return True
        if self.__ranks[root_u] > self.__ranks[root_v]:
            self.__parents[root_v] = root_u
        elif self.__ranks[root_v] > self.__ranks[root_u]:
            self.__parents[root_u] = root_v
        else:
            self.__parents[root_u] = root_v
            self.__ranks[root_v] += 1
        return False

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def components(self):
        components = defaultdict(list)
        for i in range(self.__len):
            components[self.find(i)].append(i)
        yield from components.values()
