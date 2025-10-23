"""
Tests for reachability module.
"""

from unittest.mock import patch

from algorythms_on_graph_py.week1_graph_decomposition.maze import (
    Maze,
)
from algorythms_on_graph_py.week1_graph_decomposition.reachability import (
    Input,
    check_path_between,
    parse_input,
)


class TestReachability:
    """Test cases for the maze exit finding algorithm."""

    def test_parse_input_sample1(self):
        """Test parsing input from sample 1."""
        # Sample 1 input:
        # 4 4
        # 1 2
        # 3 2
        # 4 3
        # 1 4
        # 1 4
        input_lines = ["4 4", "1 2", "3 2", "4 3", "1 4", "1 4"]

        with patch("builtins.input", side_effect=input_lines):
            result = parse_input()

        expected = Input(n=4, m=4, edges=[(1, 2), (3, 2), (4, 3), (1, 4)], u=1, v=4)

        assert result.n == expected.n
        assert result.m == expected.m
        assert result.edges == expected.edges
        assert result.u == expected.u
        assert result.v == expected.v

    def test_parse_input_sample2(self):
        """Test parsing input from sample 2."""
        # Sample 2 input:
        # 4 2
        # 1 2
        # 3 2
        # 1 4
        input_lines = ["4 2", "1 2", "3 2", "1 4"]

        with patch("builtins.input", side_effect=input_lines):
            result = parse_input()

        expected = Input(n=4, m=2, edges=[(1, 2), (3, 2)], u=1, v=4)

        assert result.n == expected.n
        assert result.m == expected.m
        assert result.edges == expected.edges
        assert result.u == expected.u
        assert result.v == expected.v

    def test_maze_path_exists(self):
        """Test path finding when path exists."""
        input_lines = ["4 4", "1 2", "3 2", "4 3", "1 4", "1 4"]

        with patch("builtins.input", side_effect=input_lines):
            inp = parse_input()

        # Path 1 -> 4 exists (direct connection)
        assert check_path_between(inp)

    def test_maze_no_path(self):
        """Test path finding when no path exists."""
        edges = [(1, 2), (3, 4)]  # Two disconnected components
        maze = Maze(4, 2, edges)

        # No path from 1 to 4
        assert maze.check_path_between(1, 4) is False

        # No path from 2 to 3
        assert maze.check_path_between(2, 3) is False

    def test_maze_same_vertex(self):
        """Test path finding when start and end are the same."""
        edges = [(1, 2), (2, 3)]
        maze = Maze(3, 2, edges)

        # Path from vertex to itself should be True
        assert maze.check_path_between(1, 1) is True
        assert maze.check_path_between(2, 2) is True

    def test_maze_single_vertex(self):
        """Test with single vertex (edge case)."""
        edges = []
        maze = Maze(1, 0, edges)

        # Single vertex to itself
        assert maze.check_path_between(1, 1) is True

    def test_maze_large_graph(self):
        """Test with larger graph to ensure algorithm scales."""
        # Create a chain: 1-2-3-4-5
        edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
        maze = Maze(5, 4, edges)

        # Path from 1 to 5 should exist
        assert maze.check_path_between(1, 5) is True

        # Path from 1 to 3 should exist
        assert maze.check_path_between(1, 3) is True

        # No path from 1 to 6 (doesn't exist)
        # This should not crash, just return False
        assert maze.check_path_between(1, 6) is False
