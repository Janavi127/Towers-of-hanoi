from collections import deque

N_DISKS = 3
PEGS = ("A", "B", "C")

class TowerOfHanoi:
    def __init__(self, n_disks=N_DISKS):
        self.n = n_disks
        self.start = (tuple(range(self.n, 0, -1)), (), ())
        self.goal = ((), (), tuple(range(self.n, 0, -1)))
        self.moves = [(i, j) for i in range(3) for j in range(3) if i != j]

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
    print(f"BFS Solution found in {len(path)} moves.")
