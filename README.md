# Advent of Code 2022

![](https://img.shields.io/badge/day%20📅-19-blue)	
![](https://img.shields.io/badge/stars%20⭐-20-yellow)	
![](https://img.shields.io/badge/days%20completed-10-red)	

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
| [Day 6](https://adventofcode.com/2022/day/6) | ⭐ | ⭐ |
| [Day 7](https://adventofcode.com/2022/day/7) | ⭐ | ⭐ |
| [Day 8](https://adventofcode.com/2022/day/8) | ⭐ | ⭐ |
| [Day 9](https://adventofcode.com/2022/day/9) | ⭐ | ⭐ |
| [Day 10](https://adventofcode.com/2022/day/10) | ⭐ | ⭐ |
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

16 Dec 2022: Finally, a solution! Things I learned over the last week of work include:

* My first thought was that I'd need to write some custom classes to handle the directory and file data, but then
  decided that would be unnecessary and too much work. I was wrong. I would have saved myself a lot of frustration if I
  had just written the classes at the start.
* Among the things I tried without success were `namedtuples`. I'm glad for the reminder that these exist, and I may
  well use them later in the month.
* I also learned about the `dataclass` decorator, from my spouse who is also doing AoC. I don't know enough to use them,
  but I now know they're out there.
* As it turns out, there were no recursive functions required; my custom classes took care of the nested tre structure
  automatically.
  I've left my extravagant use of print statements in place as comments, in case I try re-using this code and want to
  watch what it does as it's doing it.

### Day 8

Today looks like a good time to remind myself about numpy.
Starting with the very basics: a grid is a 2D numpy array,

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

### Day 9

I'm so glad there was a second half of this puzzle. The first half asked us to simulate the movement of two-segment
ropes (head + tail), and I solved that pretty easily. But the second half involves longer ropes, and my solution didn't
work. It turns out that my mental model for how the tail moved was wrong -- close enough that it didn't cause errors in
the simpler first case, but not correct enough to solve a general case. Also, I used a dataclass in part of my solution,
yay!

### Day 10

I had some difficulty at first understanding the puzzle, but once I figured out what we were actually supposed to be
doing, the rest went quite smoothly. I'm sure some actual learning happened. Unfortunately, the memory of writing code
has been swallowed up by happy silly sounds in my brain.
"Noop" probably means something practical, like "no operation". But I hear it as a cute little sound, to rhyme with "
goop". I kind of want a new pet now, so I can name them "Noop" and just boop their little snoot.

### Interlude: Wrapper script

Just for fun, I've been working on a script I can run when I want to review the Advent of Code frame story -- this year,
about elves gathering starfruit. Now I can look at all of my solutions in order, as many as I want, without having to
return to the command line.

Among other things, I learned that naming my wrapper `__main__.py` means I can call it using the name of the package
directory it's in. Along the way I've also learned a little about importing modules. I tried using relative import paths
but had difficulty handling the fact that my solutions can be run as standalone scripts as well as being imported into
the wrapper script. In the end, I discovered a nice combination that worked: `pyprojroot.here()` to give a stable anchor
for the whole project, and `pydoc.importfile()` to handle the dynamic import from filename. That is so much easier! 
