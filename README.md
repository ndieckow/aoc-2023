# Advent of Code 2023
My solution for this year's Advent of Code in Python. Like [last year](https://github.com/ndieckow/aoc2022), I'll try to write a few words about each solution, both focusing on my performance and the complexity of my solutions.

In general, $N$ always refers to the number of lines in the input. If not, I will mention it.

## Leaderboard Ranks

Day | Part 1 | Part 2 | Comment
----|--------|--------|--------
1   | 22673  | 13824  |
2   | 3407   | 3047   |
3   | 5376   | 3456   |
4   | 304    | 313    |
6   | 659    | 3797   |
7   | 600    | 391    |
8   | 342    | 325    |
9   | 13455  | 13149  |

## Day 01
For part 1, the complexity is $\mathcal O(N \cdot \ell)$, where $\ell$ is the length of the longest string. Assuming it to be constant, we have linear complexity, $\mathcal O(N)$. For part 2, we have an additional loop through all one-digit numbers, but since there's always exactly 10 of them, the complexity remains linear.

## Day 02
$\mathcal O(N)$. I initially missed the part about returning the cubes after each set is drawn, which cost me some time. Didn't get on the leaderboard.

## Day 03
It started off so great. I was ready to submit an answer after around 11 minutes, which would have guaranteed me a place in the top 1000. But my answer was wrong, even though it worked on the example. Trying to figure this bug out cost be a BUNCH of time. It turned out that I forgot to consider the case that the same number could show up in two different places. My approach was suboptimal from the start, anyway. I considered the symbols as "central" and looked at *its* neighbors, instead of going the other way around and finding all numbers and checking *their* neighborhood for symbols.

Anyway, let $S$ be the number of cells in which there is a symbol, and $N$ the total number of... numbers. The number of rows and columns are $R$ and $C$, respectively. Also, let $\ell$ be the number of digits of the longest number. Scanning for symbols is $\mathcal O(R C)$. Because the number of possible adjacent numbers is bounded, figuring out the neighbors of all symbols is $\mathcal O(S \ell)$. So, $\mathcal O(RC + S\ell)$ in total. So, we don't actually need $N$ in this consideration.

Using the (very coarse) bounds $S \leq RC$ and $\ell \leq C$, we find that the algorithm has complexity $\mathcal O(RC^2)$. At the same time, if all grid values are filled with symbols, there are no numbers left anymore, i.e. $\ell = 0$. So, can we maybe lower the complexity? I don't think so. Consider the (admittedly stupid) example of the first row consisting of a long number, and all of the other cells containing symbols. We still have $S = \mathcal O(RC)$ and $\ell = C$. I'm sure you can construct some nontrivial examples as well.

(Side note: The number-centric view would yield a $\mathcal O(RC + N \ell)$ algorithm. Since it appears that $N \approx \mathcal O(S)$, the two algorithms are similar in terms of complexity. Of course, the actual performance depends on the overheads.)

My solution for part 2 has the same complexity, but could maybe be done faster, as we don't have to check all symbols. Here, the symbol-centric view might actually be advantageous.

## Day 04
Today went a lot better! I was reasonably quick and finished both problems in under ten minutes, giving me ranks 304 and 313 for both parts, respectively. It's not top 100, but it's good enough to be mentioned on the solution page.

For the complexity, let $N$ be the number of cards, $n_{\mathrm{win}}$ the number of winning numbers and $n_{\mathrm{own}}$ those that you have. All of the `split`s are linear in the length of the line, which is equivalent to $\mathcal O(n_\mathrm{win} + n_\mathrm{own})$, assuming that the numbers are not unbounded. The complexity of set intersection grows linearly in the smaller set, i.e. the winning numbers. In total, we have $\mathcal O(N m)$ where I've set $m \coloneqq n_\mathrm{win} + n_\mathrm{own}$. Part 2 has the same complexity: The "additional cards" thing is handled by integer arithmetic, and the lack of intersection does not reduce the complexity because we still need to process the input.

## Day 05
soon

## Day 06
Let $T$ and $D$ denote the values for time and distance, respectively.
For part 1, I just looped through all of the values. The complexity is thus $\mathcal O(T)$. You can better with binary search. Part 2 would have also worked with this algorithm (maybe 10s with ordinary Python on an Apple M1). I just solved the equation $x (T-x) = 0$ with solutions $x_{+,-} = \frac{T}{2} \pm \sqrt{\frac{T^2}{4} - D}$ and counted the number of integers in-between the solutions by doing $\lfloor x_+ \rfloor - \lceil x_- \rceil + 1$.

## Day 07
Sweet problem. I noticed that my mental pace wasn't at its peak today and decided to take it slow, but surprisingly still placed 600th and 391th in parts 1 and 2, respectively.
I think the best approach is to store all information in a well-chosen state, and then let a sorting algorithm do all the sorting. For part 1, I chose `(kind, others_same, hand_emb, bid)`, where `hand_emb` is just an embedding of the space of cards into the space of integers according to the desired card order. This embedding differs between both parts. Having hte bid in the state is not necessary, but it's convenient for computing the solution.

Because of the sorting, the complexity is $\mathcal O(N \log N)$.

## Day 08
I'll have to think about the complexity a bit. It's too simple to say that it depends linearly on the size of the graph, because the problem is so dependent on the graph's structure.

Overall a nice problem, requiring a bit of thought for the second part, because the brute-force approach doesn't work anymore.

## Day 09
Let $\ell$ be the length of the history (i.e. how many numbers) and $d$ the number of times you can take the differences until you reach all zeros. We may assume $d \leq \ell$. For a particular line, the complexity of repeatedly taking differences is $$\sum_{i=1}^d \ell - i = d\ell - \sum_{i=1}^d i = d\ell - \frac{d(d+1)}{2},$$ which is $\mathcal O(\ell^2)$ in the worst case (the worst case being $d = \ell$).

Including all lines, the overall worst-case complexity for both parts is then $\mathcal O(N \ell^2)$.