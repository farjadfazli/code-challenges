"""
Counting Dinosaurs

You are given a string animals and another string dinosaurs. Every letter in animals represents a different type of animal and every unique character in dinosaurs represents a different dinosaur.

Return the total number of dinosaurs in animals.
Example 1

Input

animals = "abacabC"
dinosaurs = "bC"

Output

3

Explanation

There's two types of dinosaurs "b" and "C". There's 2 "b" dinosaurs and 1 "C" dinosaur. Note we didn't count the lowercase "c" animal as a dinosaur.
"""
class Solution:
    def solve(self, animals, dinosaurs):
        from collections import Counter
        dinosaurs = set(dinosaurs)
        counter = 0
        animalsDict = Counter(animals)
        print(animalsDict)
        for i in dinosaurs:
            counter += animalsDict[i]
        return counter