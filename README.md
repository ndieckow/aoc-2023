# Advent of Code 2023
My solution for this year's Advent of Code in Python. Like [last year](https://github.com/ndieckow/aoc2022), I'll try to write a few words about each solution, mainly focusing on the complexity.

In general, $N$ always refers to the number of lines in the input. If not, I will mention it.

## Day 01
For part 1, the complexity is $\mathcal O(N \cdot m)$, where $m$ is the length of the longest string. Assuming it to be constant, we have linear complexity. For part 2, we have an additional loop through all numbers, but since they're bounded, the complexity remains linear.