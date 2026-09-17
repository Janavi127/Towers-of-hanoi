# Tower of Hanoi 

## Project Description
The **Tower of Hanoi State Space Search** project is a Python program that solves the classic Tower of Hanoi puzzle using two uninformed graph search algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.

The program represents each peg configuration as a state, explores the state space using both search strategies, and compares them on:

- Path length (number of moves)
- Number of nodes expanded
- Whether the solution found is optimal

**Registration No.:** 15217

##  Objective
The main objective of this project is to demonstrate **uninformed state-space graph search** using Python, and to compare BFS and DFS on the same problem.

The program evaluates search strategies based on:

- **Branching Factor** – how many valid moves are available from a state.
- **Search Depth** – how many moves deep the goal is found.
- **Node Expansion** – how many states each algorithm visits before finding the goal.

##  Search Agent Concept
A search agent explores a state space to find a path from an initial state to a goal state.

In this project:

**States / Percepts:**
- Current configuration of disks across Peg A, Peg B, and Peg C

**Actions:**
- Move the top disk of any non-empty peg onto another peg, if that peg is empty or its top disk is larger

**Goal Test:**
- All disks are stacked in order on Peg C → `((), (), (4, 3, 2, 1))`

**Search Strategy:**
- BFS explores the state space level by level (FIFO queue)
- DFS explores one branch deeply before backtracking (stack)
- A `visited` set is used in both to avoid revisiting states

##  Path Cost Calculation
Each move has a uniform cost of 1. The total path cost is the number of moves taken to reach the goal.

**Example**

For `N = 4` disks:
- Theoretical minimum moves = `2^N − 1 = 15`
- Total reachable states = `3^N = 81`

```
BFS Path Cost = 15 (optimal)
DFS Path Cost = 27 (sub-optimal)
```

##  Technologies Used
- Python 3
- Tuples (for immutable state representation)
- Queue (BFS) and Stack (DFS)
- Sets (visited-state tracking)
- Functions and loops
- Basic complexity analysis

##  Project Structure
```
Tower-of-Hanoi-Search/
│
├── src/
│   └── hanoi_search.py
│
├── tests/
│   └── test_hanoi_search.py
│
└── README.md
```
If your Python file is currently in the root folder instead of `src/`, move it into the `src` folder to match the required project structure.

##  How to Run

**1. Install Python**
Make sure Python 3 is installed on your computer.

Check the Python version:
```
python --version
```

**2. Clone the Repository**
```
git clone YOUR_GITHUB_REPOSITORY_URL
```

**3. Open the Project**
```
cd Tower-of-Hanoi-Search
```

**4. Run the Program**
If the file is inside `src`:
```
python src/hanoi_search.py
```

##  Sample Input
```
Enter number of disks: 4
```

##  Sample Output
```
Register: 15217 | Disks: 4 | Total States: 81
BFS: 15 moves (Optimal) | Expanded Nodes: 81
DFS: 27 moves           | Expanded Nodes: 31

========== SHORTEST SOLUTION STEPS (BFS) ==========

Step  1: Move Disk 1 from A to B
Step  2: Move Disk 2 from A to C
...
Step 15: Move Disk 1 from B to C
```
The exact expanded-node count for DFS depends on the move ordering used in the implementation.

##  Working Process
```
Start
  ↓
Enter number of disks (N)
  ↓
Generate initial state ((N,...,2,1), (), ())
  ↓
Run BFS: explore level by level
  ↓
Run DFS: explore depth-first with backtracking
  ↓
Track visited states to avoid cycles
  ↓
Record path length and expanded nodes for each
  ↓
Compare BFS and DFS results
  ↓
Display move sequence and metrics
  ↓
End
```

## Features
- Solves Tower of Hanoi for any number of disks (N)
- Implements both BFS and DFS as graph search (not tree search)
- Prevents infinite loops using a visited-state set
- Calculates and displays total reachable state space (`3^N`)
- Compares optimality, path length, and nodes expanded
- Displays the full optimal move sequence from BFS

##  Search Comparison Rules
| Factor | BFS | DFS |
|---|---|---|
| Exploration order | Level by level | Deepest branch first |
| Optimality | Guaranteed | Not guaranteed |
| Nodes expanded | Higher (explores full space) | Lower (stops at first goal found) |
| Memory usage | Higher (stores full frontier) | Lower (stores current path) |

BFS therefore guarantees the shortest solution, while DFS may reach a solution faster in terms of nodes expanded but with a longer path.

##  Limitations
This is a basic uninformed-search implementation. Some limitations are:

- Only practical for small values of N, since the state space grows as `3^N`
- DFS solution quality depends heavily on move ordering
- No heuristic is used, so search is not goal-directed
- Does not visualize the peg movements graphically
- Only supports the standard 3-peg Tower of Hanoi variant

##  Future Enhancements
Possible improvements include:

- Add A* search with an admissible heuristic for comparison
- Add iterative deepening DFS (IDDFS)
- Visualize disk movements with a GUI or animation
- Support the 4-peg (Frame–Stewart) variant
- Track and plot runtime alongside expanded nodes
- Add unit tests for state transitions and goal checking

## Learning Outcomes
Through this project, the following concepts are demonstrated:

- Python programming
- State-space representation using tuples
- Graph search vs tree search
- BFS and DFS implementation
- Cycle avoidance using visited sets
- Optimality proofs for uniform-cost search
- Time and space complexity analysis (Big-O)

## 👨‍💻 Author
janavi.v

## 📄 License
This project is created for academic/educational purposes.

