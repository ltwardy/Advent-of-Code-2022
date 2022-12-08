# Advent of Code 2022

![](https://img.shields.io/badge/day%20📅-5-blue)	
![](https://img.shields.io/badge/stars%20⭐-10-yellow)	
![](https://img.shields.io/badge/days%20completed-5-red)	

My solutions for Advent of Code 2022, as I write them.

<!--- advent_readme_stars table --->
## 2022 Results

| Day | Part 1 | Part 2 |
| :---: | :---: | :---: |
| [Day 1](https://adventofcode.com/2022/day/1) | ⭐ | ⭐ |
| [Day 2](https://adventofcode.com/2022/day/2) | ⭐ | ⭐ |
| [Day 3](https://adventofcode.com/2022/day/3) | ⭐ | ⭐ |
| [Day 4](https://adventofcode.com/2022/day/4) | ⭐ | ⭐ |
| [Day 5](https://adventofcode.com/2022/day/5) | ⭐ | ⭐ |
<!--- advent_readme_stars table --->

## Some notes along the way...

### Day 1

Solving the puzzles was easy, but using GitHub is still clumsy and non-intuitive. Keep practicing.

### Day 2

My solution is broken into lots of little functions; this makes it easy for me to keep track of what I'm doing while I'm
writing, but I'm not sure whether it helps the reader. It will be interesting to see how my style changes over the
month, as puzzles get more difficult.

### Day 3

This looks like a great chance to practice using list comprehensions. As I get more familiar with writing these clever
and compact code structures, I hope they'll be easier to read.

### Day 4

This puzzle felt surprisingly easy; I hope that I'm as pleased when I look back at this code later as I am today. My
solution would probably be too memory-intensive for large data sets (looking at you, day 22 of 2021) but for the actual
puzzle data today it was just fine.

I'm working on a wrapper script, just for fun, to make it easy to run multiple AoC solutions in an interactive session.
This wouldn't be so hard if I hardcoded the paths to all the relevant files, but wouldn't it be great to use relative
paths instead? That turns out not to be a trivial problem. I need to learn about pathlib until it makes sense.

### Day 5

I feel so rusty. Lots of my solving time today was actually looking up things like 'rstrip' and shortcutting with
boolean operators. Once I got the input file parsed, the rest of the puzzle wasn't bad.

### Day 6

The solution to this puzzle was pretty straightforward, but it took me an hour of careless mistakes and chasing ideas
for "improvements" that didn't actually work to write six lines of successful code. That's a demonstration, if I needed
one, of the cognitive effects of inadequate sleep. If I want to be able to code in the morning, I need to go to bed on
time.

### Day 7

Traversing trees is interesting but still non-intuitive for me. Can I write a recursive solution? I'll come back to this
when I have more contiguous time to work on it.

### Day 8

Today looks like a good time to remind myself about numpy.
Starting with the very basics: if grid is a 2D numpy array,

* grid[0] is the first row.
* grid[0: 2] is the 3rd column, because we count from zero.
* grid[0,2] is the element found in the first row, third column position.
* grid.shape is a tuple (number of rows, number of columns).

I found it helpful to read that in numpy, the last coordinate is the one that changes fastest. If I'm watching the
indices change as I traverse an array, the last digit changes first: that's which column we're in. Then, when we run out
of columns, we go to a new row, and that coordinate comes first. It's like place value, only instead of ones >> tens >>
hundreds >> thousands, it's columns >> rows >> planes >> spaces >> multiverses. I hope thinking of lower-dimension
arrays spatially like this will make higher-dimensional arrays easier to work with.

All in all, today's puzzle was less painful than I expected. Also, I like these elves' ideas about tree houses. I'd love
to visit their house that can see a *lot* of trees <3