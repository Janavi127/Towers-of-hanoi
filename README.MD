# Tower of Hanoi Search Model → Robotic Container-Stacking Planner

## Project Description
This project extends the classic **Tower of Hanoi State Space Search** into a **Robotic Container-Stacking Planner**. It is a Python program that combines four AI techniques in one pipeline:

- **Uninformed search** – BFS and DFS on Tower of Hanoi
- **STRIPS planning** – a generic planner for Hanoi and Blocks World (robot arm)
- **Constraint Satisfaction (CSP)** – backtracking, forward checking and MRV to decide which stack each container goes on
- **Safety checking and explanation** – the arm never lifts an overweight container, and every action is explained

**Registration No.:** 15217 (in the code; used to seed the random move order and set the number of disks)

## Objective
To show how a basic state-space search model grows into a practical planner, and to compare:

- BFS vs DFS (path length, nodes expanded, optimality)
- STRIPS planning vs plain BFS on the same Hanoi problem
- Plain backtracking vs forward checking vs forward checking + MRV (assignments tried, runtime)

## Planning Agent Concept
**States / Percepts**
- Hanoi: configuration of disks on pegs A, B, C
- Robot arm: a set of facts such as `On(x,y)`, `OnTable(x)`, `Clear(x)`, `Holding(x)`, `ArmEmpty`

**Actions**
- Hanoi: `Move(disk, from, to)` if the target is empty or has a larger top disk
- Robot arm: `Pickup`, `Putdown`, `Stack`, `Unstack`

**Goal Test**
- Hanoi: all disks on peg C
- Container stacking: all stack relations chosen by the CSP are true

**Path Cost**
- Every action costs 1; BFS therefore returns the plan with the fewest actions. For `N` disks the minimum is `2^N − 1` moves (15 for `N = 4`), and the state space has `3^N` states (81 for `N = 4`).

## CSP Rules for Stacking
- Two hazardous containers never share a stack
- Heavier containers go below lighter ones that depart no earlier: `(w1 − w2)(t1 − t2) ≥ 0`
- A stack cannot exceed its maximum height
- Containers heavier than the arm limit are never picked up (no `Pickup`/`Unstack` action is generated, and the plan runner re-checks every step)

## Technologies Used
- Python 3 (standard library only: `random`, `time`, `collections.deque`, `dataclasses`)
- Tuples and frozensets (immutable states)
- Queue (BFS) and stack (DFS)
- Backtracking, forward checking, MRV heuristic

## Project Structure
```
Tower-of-Hanoi-Container-Planner/
│
├── src/
│   └── main.py
│
├── tests/
│   └── test_main.py
│
└── README.md
```

## How to Run

**1. Check Python**
```
python --version
```

**2. Clone the Repository**
```
git clone YOUR_GITHUB_REPOSITORY_URL
cd Tower-of-Hanoi-Container-Planner
```

**3. Run the Program**
```
python src/main.py
```

**4. Run the Tests**
```
python -m unittest discover tests
```

## Sample Output
```
Register: 15217 | Disks: 4 | States: 81
BFS: 15 moves (optimal), nodes=81
DFS: 15 moves, nodes=16

Hanoi via STRIPS: 15 moves, 68 nodes
Hanoi via BFS:    15 moves, 81 nodes (lengths should match)

blocks   plan    nodes
     3      4       19
     4      6      108
     5      8      771

  n stacks plain tried  FC tried   FC+MRV
 12      4          12        12       12
 18      5         603       264       18
 18      6         590       419       18

CSP stack assignment (bottom -> top): [['C5', 'C2', 'C1'], ['C4', 'C3'], ['C6']]
Robot plan: 6 actions
Goal verified: all required stack relations are satisfied.
```
Runtimes are also printed and vary by machine; the counts above are deterministic. DFS's result depends on the move ordering, so it is not guaranteed to be optimal.

## Working Process
```
Start
  ↓
Compute disks N from the register number
  ↓
Solve Hanoi with BFS and DFS → compare moves and nodes
  ↓
Solve Hanoi with the STRIPS planner → compare with BFS
  ↓
Run Blocks World scaling (3, 4, 5 blocks)
  ↓
Compare CSP methods: plain / forward checking / FC + MRV
  ↓
Generate containers → CSP chooses goal stacks
  ↓
STRIPS planner builds the arm plan → safety check → explanation
  ↓
End
```

## Features
- BFS (optimal) and DFS with a visited set (graph search)
- Generic STRIPS planner with an explanation for every step
- Hanoi and Blocks World action domains with input validation
- CSP solver with forward checking and optional MRV
- Robot-arm weight limit enforced twice (when generating actions and when running the plan)
- Comparison experiments with assignments tried and runtime

## Comparison Summary
| Factor | BFS | DFS |
|---|---|---|
| Optimality | Guaranteed | Not guaranteed |
| Nodes expanded (N = 4) | 81 | 16 |
| Memory | Higher | Lower |

| CSP method | Idea | Assignments (18 containers, 5 stacks) |
|---|---|---|
| Plain backtracking | Try values in order | 603 |
| Forward checking | Remove conflicting values early | 264 |
| FC + MRV | Also pick the most constrained container first | 18 |

## Limitations
- BFS over fact sets grows quickly as the number of containers rises
- The arm holds one container at a time; no travel cost or crane geometry
- Test instances are small and randomly generated
- No graphical visualisation

## Future Enhancements
- A* search with a heuristic for the planner
- Multiple arms and movement-time costs
- Graphical simulation of the container yard
- Runtime plots for larger inputs

## Learning Outcomes
- State-space search (BFS, DFS) and optimality
- STRIPS planning with preconditions and effects
- Constraint satisfaction with forward checking and MRV
- Safety constraints and explainable plans
- Writing unit tests for AI algorithms

## 👨‍💻 Author
janavi.v

## 📄 License
This project is created for academic/educational purposes.