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

    def search(self, mode="bfs"):
        container = deque([self.start])
        visited = {self.start: (None, None)}
        expanded = 0

        while container:
            curr = container.popleft() if mode == "bfs" else container.pop()
            expanded += 1
            if curr == self.goal:
                path, node = [], curr
                while visited[node][0]:
                    node, move = visited[node]
                    path.append(move)
                return path[::-1], expanded

            for nxt, move in self.get_neighbors(curr):
                if nxt not in visited:
                    visited[nxt] = (curr, move)
                    container.append(nxt)


if __name__ == "__main__":
    game = TowerOfHanoi()
    bfs_path, bfs_nodes = game.search("bfs")
    dfs_path, dfs_nodes = game.search("dfs")

    print(f"Register: {REG_NO} | Disks: {N_DISKS} | Total States: {3**N_DISKS}")
    print(f"BFS: {len(bfs_path)} moves (Optimal) | Expanded Nodes: {bfs_nodes}")
    print(f"DFS: {len(dfs_path)} moves           | Expanded Nodes: {dfs_nodes}\n")

    print("Shortest Solution Steps (BFS):")
    for i, (src, dst, disk) in enumerate(bfs_path, 1):
        print(f"Step {i:2d}: Move Disk {disk} from {PEGS[src]} to {PEGS[dst]}")
