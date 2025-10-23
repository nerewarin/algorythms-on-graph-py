"""
Standalone version of reachability.py which not imports any other module following submit assignment rules :(
"""

import collections
import dataclasses
from functools import cached_property
from typing import Dict, Generator, Iterator, List, Optional, Set, Tuple

# Use int for vertex IDs - simpler and more convenient
# Python 3.6.9 compatible type aliases
Edge = Tuple[int, int]
EdgesList = List[Edge]
AdjList = Dict[int, List[int]]


class Maze:
    def __init__(self, n: int, m: int, edges: EdgesList) -> None:
        # vertexes_amount
        self.n = n
        # edges_amount
        self.m = m
        self.edges = edges

    @property
    def vertexes(self) -> Generator[int, None, None]:
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

    def _explore(self, v: int, visited: Optional[Set[int]] = None) -> Set[int]:
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

    def _dfs(self) -> Tuple[Set[int], int]:
        visited: Set[int] = set()
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


def parse_input_line(type_: Optional[type] = int) -> Iterator[int]:
    if not type_:
        type_ = int
    return map(type_, input().split())


@dataclasses.dataclass
class Input:
    n: int
    m: int
    edges: EdgesList
    u: int
    v: int


def parse_input() -> Input:
    n, m = parse_input_line()
    edges = []
    for _ in range(m):
        u_edge, v_edge = parse_input_line()
        edge = (u_edge, v_edge)
        edges.append(edge)
    u, v = parse_input_line()
    return Input(n, m, edges, u, v)


def check_path_between(inp: Input) -> bool:
    maze = Maze(inp.n, inp.m, inp.edges)
    return maze.check_path_between(inp.u, inp.v)


if __name__ == "__main__":
    inp: Input = parse_input()
    res = check_path_between(inp)
    print(res)
