# Advent of Code 2023
My solution for this year's Advent of Code in Python. Like [last year](https://github.com/ndieckow/aoc2022), I'll try to write a few words about each solution, both focusing on my performance and the complexity of my solutions.

In general, $N$ always refers to the number of lines in the input. If not, I will mention it. Same holds for $R$ and $C$ (rows and columns) when dealing with grids.

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
For part 1, it is sufficient to sort the ranges by the second coordinate (a.k.a. the start of the source range) and then go through the ranges in order. Let $R_{x,y}$ be the number of ranges from the $x \to y$ map (where, e.g., $x$ could be `seed` and $y$ could be `soil`). Then, the worst case time complexity for part 1 is $\mathcal O(\sum_{x,y} R_{x,y} \log R_{x,y})$, since most of the work is sorting. More simply, by letting $R = \max_{x,y} R_{x,y}$, we just get $\mathcal O(R \log R)$ (since we assume the number of transformations to be part of the problem and thus constant).

For part 2, it is infeasible to apply the above approach to each number in the ranges. Instead, we need to transform the ranges as a whole. In the $x \to y$ step, we transform a number of $n$ ranges in $R_{x,y}$ roughly constant-time steps. Each $x \to y$ step on a single range can potentially produce up to $2R_{x,y}+1$ intervals. So, we would theoretically end up with $\sum_{k=1}^6R(2R+1)^k = \mathcal O(R^7)$ steps. However, as there are only $R$ intersections to consider, we can at each transformation only gain at most $2R$ additional ranges *in total*, not for all ranges. This would give us instead at most $R (1 + \sum_{k=1}^6 k2R) = \mathcal O(R^2)$ many steps.

## Day 06
Let $T$ and $D$ denote the values for time and distance, respectively.
For part 1, I just looped through all of the values. The complexity is thus $\mathcal O(T)$. You can better with binary search. Part 2 would have also worked with this algorithm (maybe 10s with ordinary Python on an Apple M1). I just solved the equation $x (T-x) = 0$ with solutions $x_{+,-} = \frac{T}{2} \pm \sqrt{\frac{T^2}{4} - D}$ and counted the number of integers in-between the solutions by doing $\lfloor x_+ \rfloor - \lceil x_- \rceil + 1$.

## Day 07
Sweet problem. I noticed that my mental pace wasn't at its peak today and decided to take it slow, but surprisingly still placed 600th and 391th in parts 1 and 2, respectively.
I think the best approach is to store all information in a well-chosen state, and then let a sorting algorithm do all the sorting. For part 1, I chose `(kind, others_same, hand_emb, bid)`, where `hand_emb` is just an embedding of the space of cards into the space of integers according to the desired card order. This embedding differs between both parts. Having hte bid in the state is not necessary, but it's convenient for computing the solution.

Because of the sorting, the complexity is $\mathcal O(N \log N)$.

## Day 08
A nice problem, requiring a bit of thought for the second part, because the brute-force approach doesn't work anymore.

The complexity analysis is a bit useless this time. Essentially, the first part is linear in the length of the path, which of course is unknown to us beforehand. Call it $\mathcal O(p)$. For part 2, let $m$ be the number of start/end node pairs. Then, the complexity is $\mathcal O(pm)$.

Ideally, we would want something as a function of $n$, the size of the graph. But in a directed graph with cycles, there are infinite paths, so a plain worst-case estimate won't help us. We might be able to work something out using the length of the instruction sequence, call it $\ell$. But even then, there will still always be graphs for which a path obtained from such a sequence is infinite.

## Day 09
Let $\ell$ be the length of the history (i.e. how many numbers) and $d$ the number of times you can take the differences until you reach all zeros. We may assume $d \leq \ell$. For a particular line, the complexity of repeatedly taking differences is $$\sum_{i=1}^d \ell - i = d\ell - \sum_{i=1}^d i = d\ell - \frac{d(d+1)}{2},$$ which is $\mathcal O(\ell^2)$ in the worst case (the worst case being $d = \ell$).

Including all lines, the overall worst-case complexity for both parts is then $\mathcal O(N \ell^2)$.

## Day 10
Not a great day for me. I actually expected a grid puzzle, but not something as gruesome as this. I took my time, but I got part 2 to work on all test inputs, yet the answer wasn't correct for the full input. Very annoying, because this puzzle is hard to debug. In fact, it's still not working. But I found the right answer, by first trying the answer $+1$, and then $+2$, which turned out to be the right answer. So there must be some really weird edge case that I'm not considering, I suppose.

I ended up solving part 2 using a clever method I found [on reddit](https://www.reddit.com/r/adventofcode/comments/18evyu9/comment/kcqipbx/). It's much shorter than flood-fill and gives the right answer. These kinds of things are the reason why it's sometimes worth to look at abstract maths, such as topology in this case.

The complexity of the first part is linear in the length of the loop. The longest possible loop in an $N \times N$ grid covers every single cell, so $N^2$.
In the second part, we just scan the grid row-by-row and column-by-column and accumulate some values. Hence, the complexity is $\mathcal O(N^2)$ for both parts.

## Day 11
Need moar sleep x.x

Took me almost an hour to get the doubling of the rows and columns right. Only to have my approach be infeasible in part 2, where I had to implement the clean method I was too lazy to think about. Even though there isn't much to think about: Since the shortest distance was just the Manhattan distance, we can walk all of the columns at once, then all the rows (or vice-versa, doesn't matter). So, to account for the expansion, we just need to count all of the empty rows and columns we pass along the way, and add that number, multiplied with the expansion constant (minus 1), onto the Manhattan distance.

The complexity is $\mathcal O(R C + N^2 m)$, where $N$ is the number of galaxies, and $m$ is the number of empty rows and columns. Technically, $m$ is a worst-case estimate: Actually, the complexity of intersecting two sets scales linearly with the size of the smaller set. You could analyze this further. There is obviously a relationship between $N$ and $m$. I wonder, if the complexity is worse than $\mathcal O((RC)^2)$.

## Day 12
DP is a good option here. For a particular instance, let $n$ be the length of the string, $k$ the number of contiguous blocks of broken springs, and $\ell$ the length of the longest such block. Then the algorithm should run in time $\mathcal O(nk\ell)$. But I'm not super sure.

## Day 13
Nasty day. At least in my opinion. According to my ranking, yesterday was apparently easier. Once again, I spent way too much time debugging stuff.

Update (19.11.24): Wrote a slightly prettier solution that's only half the size of my initial one. It first converts the blocks to NumPy Arrays of 0s and 1s, allowing me to easily transpose them. Then it's just a matter of iterating through each potential reflection line (a.k.a. row), retrieving the correct number of lines above and below the reflection line and performing an elementwise XOR. In part $i \in \{1,2\}$, the result of that XOR should be $i-1$ ;)

As for complexity, we can consider the worst case of the reflection line being in the very last row (or column). For this case, we have to iterate through $R+C-2$ potential reflection lines, where each iteration involves an operation linear in $\mathcal O(rc)$, where $r$ and $c$ are the dimension of the considered sub-arrays. However, only one of the dimensions is different from $R$ and $C$. In total this gives us a worst-case time complexity of
$$\sum_{r=1}^{R-1} \mathcal O(rC) + \sum_{c=1}^{C-1} \mathcal O(Rc) = \mathcal O(R^2 C + C^2 R) = \mathcal O(RC(R+C)).$$

## Day 14
Got the top 1000 for part 1 after a row a bad days. Quite happy about that :) Wasted a lot of time on debugging for part 2. Turned out that I wasn't thinking it through: Since we've already done a few cycles, the calculation for the number of remaining cycles is $(1000000000 - n - 1) \mod (m - n)$, where $m$ is the index where you notice repetition, and $n$ is the index where the repetition starts. I simply forgot the subtraction of $n$ and got a wrong answer.

Complexity analysis: Let $N$ denote the side length of the square grid. The crucial part is the rock-sliding, which can be done in time $\mathcal O(N^2)$. If we assume the number of cycles until it loops to be constant, this still holds up for part 2. 

## Day 15
An easier problem, compared to the previous days. There was more of a focus on reading comprehension and computer science education, which is cool. For some reason, I thought sorting would be involved, so the members of my boxes look like (value, key) instead of (key, value). Does not really matter, though.

Let $N$ be the number of (comma-separated) instructions. Hash computation (part 1) is linear in the string length. If we assume that all strings are bounded in length, part 1 is just linear in $N$.

For part 2, let's first consider the operation level. Let $\ell$ the the length of the label. Both insertion (`a=1`) and deletion (`a-`) require hashing, which is $\mathcal O(\ell)$. Let $b$ be the number of elements in the considered box. Checking whether the label is already present is $\mathcal O(b)$. So, insertion and deletion both have a complexity of $\mathcal O(\ell + \max b)$. However, in practice, we rarely use labels with unbounded length, and the hash function is chosen in such a way that it equally distributes amongst all boxes, so that their size is kept small. Both of these assumptions yield $\mathcal O(1)$ armortized time complexity for both insertion and deletion.
So in total, $\mathcal O(N)$ for part 2 as well.

## Day 16
Viewing nodes as having both position $(r,c)$ and direction $(dr,dc)$, this is essentially just a DFS. As there are 4 possible directions, we have $4RC = \mathcal O(RC)$ many nodes and, due to the grid structure, also only $\mathcal O(RC)$ many edges. So, the algorithm for part 1 has a time complexity of $\mathcal O(RC)$ in total.

For part 2, we need to iterate over $2R+2C$ starting points, so the complexity here is $\mathcal O(RC(R+C)).$

## Day 17
Just Dijkstra. The number of nodes $V$ is $2RC$, and Dijkstra's algorithm has a complexity of $\mathcal O(\lvert E\rvert \log \lvert V\rvert)$. Each node has at most $6$ neighbors in part 1, and at most $14$ in part 2. We call this constant $k$. By the handshake lemma,
$$2\lvert E\rvert = \sum_{v \in V} \deg(v) \leq \lvert V \rvert k,$$
so that $\lvert E \rvert = \mathcal O(\lvert V \rvert)$, giving us a complexity of $\mathcal O(RC \log (RC))$ for both parts.

## Day 18
Did a floodfill for part 1. However, for part 2, this is not fast enough. Luckily, the [shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula) comes to the rescue. The formula gives you the area in linear time, at least in $\R^2$. However, you would like something like
```
##
##
```
to be counted as $4$ and not $1$, so we have to add $B/2 + 1$ to the result, where $B$ is the number of boundary points, which we can easily compute from the instructions. To be honest, I just guessed the term, and it turned out correct. Note that $B$ is always an even number, due to the restriction to straight boundaries.

Both parts: $\mathcal O(N)$

## Day 19
Rough past days. Will eventually do a writeup on those. Today was better. Funnily, I had the exact same rank in both parts, which was not much over 1000.
I think both parts are linear in the length of the procedure, but I haven't done a thorough analysis. We're basically just going through each step. Of course, when considering ranges, we're considering all paths, so it's linear in the number of possible paths... which we don't know, so this analysis is kind of useless.

## Day 20
Today was a bit nasty. The problem was interesting, but tricky to implement. Had to do lots of debugging in part 1. Part 2 required a minimal amount of reverse engineering and some elementary number theory. My code is not generic, because the `interest` array is hardcoded. Despite taking quite long, I still placed below 1000 in both parts.

## Day 21
Part 1 is a slightly modified BFS. The nodes are augmented by the remaining steps, which allows us to detect odd/even steps, and add the correct ones to a collection, the length of which we can query to obtain the answer in the end. For part 2, we can re-use this function (call it $S$) to get the number of cells after $n$, $n + R$ and $n + 2R$ steps, where $n = 26501365 \% R$. Define a sequence by $x_i = S(n + iR)$ for $i \geq 0$. It turns out that this sequence is of the form $x_i = a i^2 + b i + c$ for some constants $a,b,c \in \mathbb Z$. We can determine them with Gaussian elimination. The answer for part 2 is then given by $x_i$ with $i = \lfloor 26501365 / R \rfloor$.

## Day 23
For some reason, I really struggled with today's problem. Setting up the graph in part 1 took me over an hour. I tried DP for the second part, but it seems like it's too slow.

Okay, DP worked for part 2, but it takes like 5 minutes. This is the solution I'm gonna go with for now. I might update this later once I figure out a faster one.

## Day 24
A different kind of problem today, requiring a bit of linear (and nonlinear) algebra. For part 1, we just iterate over all pairs of hailstones and solve a 2-by-2 system in constant time. So, $\mathcal O(N^2)$ overall.

For part 2, you can build a big nonlinear system with 900 equations (3 equations for each hailstone) and 306 unknowns (3 for position + 3 for velocity + the collision times with the 300 hailstones). You can apparently plug this into Z3 and get the solution. I tried sympy, but it never finished. Luckily, there is a simplification: If you think about it, you'll realize you only need three equations to determine a straight line in $\R^3$. We know that a solution exists, so if it works for three, it must work for all hailstones. With just 9 equations and 9 unknowns, sympy finishes quickly. But I don't know how it operates (probably some crazy computational algebra), so I can't give a complexity estimate.

I've also tried using Newton's method, but it's very fickle. The initial guess `np.arange(9) * 100000` works best for me (the constant was chosen arbitrarily, you just want to be somewhat close to the true solution). With an ample 39 iterations, it converges to the correct solution, at least on my input.

## Missing Estimates
* Day 19
* Day 20
* Day 21
* Day 22
* Day 23