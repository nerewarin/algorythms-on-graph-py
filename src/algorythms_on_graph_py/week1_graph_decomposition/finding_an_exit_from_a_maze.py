"""
Problem Description
Task. Given an undirected graph and two distinct vertices 𝑢 and 𝑣, check if there is a path between 𝑢 and 𝑣.
Input Format. An undirected graph with 𝑛 vertices and 𝑚 edges. The next line contains two vertices 𝑢
and 𝑣 of the graph.
Constraints. 2 ≤ 𝑛 ≤ 103; 1 ≤ 𝑚 ≤ 103; 1 ≤ 𝑢, 𝑣 ≤ 𝑛; 𝑢 ̸= 𝑣.
Output Format. Output 1 if there is a path between 𝑢 and 𝑣 and 0 otherwise.
Time Limits.
language C C++ Java Python C# Haskell JavaScript Ruby Scala
time (sec) 1 1 1.5 5 1.5 2 5 5 3
Memory Limit. 512MB.
Sample 1.
Input:
4 4
1 2
3 2
4 3
1 4
1 4
Output:
1
1 2
4 3
In this graph, there are two paths between vertices 1 and 4: 1-4 and 1-2-3-4.
5
Sample 2.
Input:
4 2
1 2
3 2
1 4
Output:
0
1 2
4 3
In this case, there is no path from 1 to 4.
Starter Files
The starter solutions for this problem read the input data from the standard input, pass it to a blank
procedure, and then write the result to the standard output. You are supposed to implement your algorithm
in this blank procedure if you are using C++, Java, or Python3. For other programming languages, you need
to implement a solution from scratch. Filename: reachability
What To Do
To solve this problem, it is enough to implement carefully the corresponding algorithm covered in the lectures.
"""
