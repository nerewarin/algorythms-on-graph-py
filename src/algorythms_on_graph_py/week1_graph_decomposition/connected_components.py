"""
2 Adding Exits to a Maze
Problem Introduction
Now you decide to make sure that there are no dead zones in a maze, that is, that at least one exit is
reachable from each cell. For this, you find connected components of the corresponding undirected graph
and ensure that each component contains an exit cell.
Problem Description
Task. Given an undirected graph with 𝑛 vertices and 𝑚 edges, compute the number of connected components
in it.
Input Format. A graph is given in the standard format.
Constraints. 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑚 ≤ 103.
Output Format. Output the number of connected components.
Time Limits.
language C C++ Java Python C# Haskell JavaScript Ruby Scala
time (sec) 1 1 1.5 5 1.5 2 5 5 3
Memory Limit. 512MB.
Sample 1.
Input:
4 2
1 2
3 2
Output:
2
1 2
4 3
There are two connected components here: {1, 2, 3} and {4}.
"""

import dataclasses

from algorythms_on_graph_py.week1_graph_decomposition.maze import EdgesList, Maze, parse_input_line


@dataclasses.dataclass
class Input:
    n: int
    m: int
    edges: EdgesList


def parse_input() -> Input:
    n, m = parse_input_line()
    edges = []
    for _ in range(m):
        u_edge, v_edge = parse_input_line()
        edge = (u_edge, v_edge)
        edges.append(edge)
    return Input(n, m, edges)


def calculate_connected_components(inp: Input) -> int:
    maze = Maze(inp.n, inp.m, inp.edges)
    return maze.calculate_connected_components()


if __name__ == "__main__":
    inp: Input = parse_input()
    res = calculate_connected_components(inp)
    print(res)
