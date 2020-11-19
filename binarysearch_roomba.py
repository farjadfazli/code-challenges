"""
Roomba

A Roomba robot is currently sitting in a cartesian plane at (0, 0). You are given a list of its moves that it will make, containing NORTH, SOUTH, WEST, and EAST.

Return whether after its moves it will end up in the coordinate (x, y).
Example 1

Input

moves = ["NORTH", "EAST"]
x = 1
y = 1

Output

True

Explanation

Moving north moves it to (0, 1) and moving east moves it to (1, 1)
Example 2

Input

moves = ["WEST", "EAST"]
x = 1
y = 0

Output

False

Explanation

This Roomba will end up at (0, 0)
"""
class Solution:
    def solve(self, moves, x, y):
        myX = 0
        myY = 0
        for move in moves:
            if move == "NORTH":
                myY += 1
            if move == "SOUTH":
                myY -= 1
            if move == "EAST":
                myX += 1
            if move == "WEST":
                myX -= 1
        return myX == x and myY == y