from collections import deque
import random

REG_NO = 15217
N_DISKS = 3 + (sum(int(d) for d in str(REG_NO)) % 3)
PEGS = ("A", "B", "C")

class TowerOfHanoi:
    def __init__(self):
        random.seed(REG_NO)
        self.moves = [(i, j) for i in range(3) for j in range(3) if i != j]
        random.shuffle(self.moves)
        
        self.start = (tuple(range(N_DISKS, 0, -1)), (), ())
        self.goal = ((), (), tuple(range(N_DISKS, 0, -1)))

    def get_neighbors(self, state):
        for src, dst in self.moves:
            if state[src] and (not state[dst] or state[dst][-1] > state[src][-1]):
                new = [list(p) for p in state]
                disk = new[src].pop()
                new[dst].append(disk)
                yield tuple(tuple(p) for p in new), (src, dst, disk)

    def bfs(self):
        queue = deque([self.start])
        visited = {self.start: (None, None)}

        while queue:
            curr = queue.popleft()
            if curr == self.goal:
                path, node = [], curr
                while visited[node][0]:
                    node, move = visited[node]
                    path.append(move)
                return path[::-1]

            for nxt, move in self.get_neighbors(curr):
                if nxt not in visited:
                    visited[nxt] = (curr, move)
                    queue.append(nxt)

if __name__ == "__main__":
    game = TowerOfHanoi()
    path = game.bfs()
    print(f"Register: {REG_NO} | Disks: {N_DISKS}")
    print(f"BFS Solution found in {len(path)} moves.")
