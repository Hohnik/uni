# KI Praktikum 03

### 1. Wooden Railways

* a) Find a connected combination of 32 rail track pieces, categorized into 4 different types, where no overlaps or lose ends occur. *(alternative: Find a combination of all rail tracks where the track forms a [unknot](https://en.wikipedia.org/wiki/Unknot) like railway.)*
* b) For the problem, I would eighter use Depth-First-Search or Breadth-Frist-Search. The complexity of the problem has a fixed branching factor of 4 and a max depth of 32. Due to the limmited depth of 32 is would use the DFS.
  * Options:
    Depth first search
    Breadth first search
    Iterative deepening search
    Bidirectional search
* c) The problem with removing one of the fork pieces is, that every fork piece adds a new track but you have to have a second piece to be able to close it again. So you can only remove even numbers of forks.

### 2. *Uniform-Cost-Search* == *A\*-Search*? 

How I understood it, Uniform-Cost-Search is just a special case of the A*-Search that has a dumb heuristic, that doesn't sort the Frontier.

Both 

