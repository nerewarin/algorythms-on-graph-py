import collections
from functools import cached_property
from typing import Generator, Optional

# Use int for vertex IDs - simpler and more convenient
type Edge = tuple[int, int]
type EdgesList = list[Edge]
type AdjList = dict[int, list[int]]


class Maze:
    def __init__(self, n: int, m: int, edges: EdgesList) -> None:
        # vertexes_amount
        self.n = n
        # edges_amount
        self.m = m
        self.edges = edges

    @property
    def vertexes(self) -> Generator[int]:
        for ind in range(self.n):
            yield ind + 1

    @cached_property
    def adjacency_list(self) -> AdjList:
        res = collections.defaultdict(list)
        for edge in self.edges:
            left, right = edge
            res[left].append(right)
            res[right].append(left)
        return res

    def _explore(self, v: int, visited: Optional[set[int]] = None) -> set[int]:
        """
        Updates visited

        Args:
            v: vertex
            visited: set of visited vertexes

        """
        if visited is None:
            visited = set()

        visited.add(v)
        for v in self.adjacency_list[v]:
            if v not in visited:
                self._explore(v, visited)

        return visited

    def _dfs(self) -> tuple[set[int], int]:
        visited: set[int] = set()
        connected_components = 0
        for v in self.vertexes:
            if v not in visited:
                self._explore(v, visited)
                connected_components += 1

        return visited, connected_components

    def check_path_between(self, u: int, v: int) -> bool:
        """
        Check if there is a path between 𝑢 and

        Args:
            u: start vertex
            v: end vertex

        Returns:
            bool

        """
        return v in self._explore(u)

    def calculate_connected_components(self) -> int:
        """
        Given an undirected graph with 𝑛 vertices and 𝑚 edges, compute the number of connected components
        in it.

        Returns:
            int

        """
        _, connected_components = self._dfs()
        return connected_components


def parse_input_line(type_: Optional[type] = int) -> map[int]:
    if not type_:
        type_ = int
    return map(type_, input().split())
