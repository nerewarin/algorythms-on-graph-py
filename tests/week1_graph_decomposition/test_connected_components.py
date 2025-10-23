"""
Tests for connected_components module.
"""

from unittest.mock import patch

from algorythms_on_graph_py.week1_graph_decomposition.for_submit.connected_components import (
    Input,
    calculate_connected_components,
    parse_input,
)


class TestReachability:
    """Test cases for the maze calculating connected components finding algorithm."""

    def test_parse_input_sample(self):
        """Test parsing input from sample 1."""
        # Sample 1 input:
        # 4 2
        # 1 2
        # 3 2
        input_lines = ["4 2", "1 2", "3 2"]

        with patch("builtins.input", side_effect=input_lines):
            result = parse_input()

        expected = Input(n=4, m=2, edges=[(1, 2), (3, 2)])

        assert result.n == expected.n
        assert result.m == expected.m
        assert result.edges == expected.edges

    def test_connected_components(self):
        inp = Input(n=4, m=2, edges=[(1, 2), (3, 2)])

        assert calculate_connected_components(inp) == 2
