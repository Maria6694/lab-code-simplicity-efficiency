"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""
import itertools
def my_function(hypothenuse):
    solutions = []
    for hypo in range(5, X):
        for cat1 in range(4, X):
            for cat2 in range(3, X):
                if (hypo*hypo==cat1*cat1+cat2*cat2):
                    solutions.append([hypo, cat1, cat2])
    m = 0
    for solution in solutions:
        if m < max(solution):
            m = max(solution)
    return m


def longest_side(max_len):
   solutions = [[x,y,z]
       for x in range(5, max_len)
       for y in range(4, max_len)
       for z in range(3, max_len)
       if (x*x==y*y+z*z)
       ]
   return max([max(solution) for solution in solutions]);
   for solution in solutions:
       if m < max(solution):
           m = max(solution)
   return m
max_len = int(input("What is the maximal length of the triangle side? Enter a number: "))
print("The longest side possible is " + str(longest_side(int(max_len))))
