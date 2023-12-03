# Advent of Code 2023
My solution for this year's Advent of Code in Python. Like [last year](https://github.com/ndieckow/aoc2022), I'll try to write a few words about each solution, both focusing on my performance and the complexity of my solutions.

In general, $N$ always refers to the number of lines in the input. If not, I will mention it.

## Day 01
For part 1, the complexity is $\mathcal O(N \cdot \ell)$, where $\ell$ is the length of the longest string. Assuming it to be constant, we have linear complexity, $\mathcal O(N)$. For part 2, we have an additional loop through all one-digit numbers, but since there's always exactly 10 of them, the complexity remains linear.

# Day 02
$\mathcal O(N)$. I initially missed the part about returning the cubes after each set is drawn, which cost me some time. Didn't get on the leaderboard.

# Day 03
It started off so great. I was ready to submit an answer after around 11 minutes, which would have guaranteed me a place in the top 1000. But my answer was wrong, even though it worked on the example. Trying to figure this bug out cost be a BUNCH of time. It turned out that I forgot to consider the case that the same number could show up in two different places. My approach was suboptimal from the start, anyway. I considered the symbols as "central" and looked at *its* neighbors, instead of going the other way around and finding all numbers and checking *their* neighborhood for symbols.

Anyway, let $S$ be the number of cells in which there is a symbol, and $N$ the total number of... numbers. The number of rows and columns are $R$ and $C$, respectively. Also, let $\ell$ be the number of digits of the longest number. Scanning for symbols is $\mathcal O(R C)$. Because the number of possible adjacent numbers is bounded, figuring out the neighbors of all symbols is $\mathcal O(S \ell)$. So, $\mathcal O(RC + S\ell)$ in total. Part 2 could probably done faster, but I don't care.

Using the (very coarse) bounds $S \leq RC$ and $\ell \leq C$, we find that the algorithm has complexity $\mathcal O(RC^2)$. At the same time, if all grid values are filled with symbols, there are no numbers left anymore, i.e. $\ell = 0$. So, can we maybe lower the complexity? I don't think so. Consider the (admittedly stupid) example of the first row consisting of a long number, and all of the other cells containing symbols. We still have $S = \mathcal O(RC)$ and $\ell = C$. I'm sure you can construct some nontrivial examples as well.