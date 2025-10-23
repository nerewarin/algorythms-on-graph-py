"""
Tests for maze module.
"""

from algorythms_on_graph_py.week1_graph_decomposition.maze import (
    Maze,
)


class TestMaze:
    """Test cases for the maze exit finding algorithm."""

    def test_maze_adjacency_list_construction(self):
        """Test that Maze correctly builds adjacency list."""
        edges = [(1, 2), (2, 3), (3, 4), (1, 4)]
        maze = Maze(4, 4, edges)

        # Check adjacency list structure
        assert len(maze.adjacency_list) == 4
        assert 2 in maze.adjacency_list[1]  # 1 connects to 2
        assert 1 in maze.adjacency_list[2]  # 2 connects to 1 (undirected)
        assert 4 in maze.adjacency_list[1]  # 1 connects to 4
        assert 1 in maze.adjacency_list[4]  # 4 connects to 1 (undirected)
