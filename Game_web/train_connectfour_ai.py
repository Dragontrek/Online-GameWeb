import random
import pickle

# Simple Q-learning for Connect Four (7x6)
class ConnectFourAI:
    def __init__(self, level='easy'):
        self.q = {}
        self.level = level
        self.epsilon = {'easy': 0.8, 'medium': 0.3, 'hard': 0.05}[level]
        self.alpha = 0.5
        self.gamma = 0.9

    def get_state(self, board):
        return tuple(tuple(row) for row in board)

    def choose_action(self, board, available):
        state = self.get_state(board)
        if random.random() < self.epsilon:
            return random.choice(available)
        qvals = [self.q.get((state, a), 0) for a in available]
        maxq = max(qvals)
        best = [a for a, qv in zip(available, qvals) if qv == maxq]
        return random.choice(best)

    def update(self, board, action, reward, next_board, next_available):
        state = self.get_state(board)
        next_state = self.get_state(next_board)
        old_q = self.q.get((state, action), 0)
        next_q = max([self.q.get((next_state, a), 0) for a in next_available] or [0])
        self.q[(state, action)] = old_q + self.alpha * (reward + self.gamma * next_q - old_q)

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.q, f)

    def load(self, filename):
        with open(filename, 'rb') as f:
            self.q = pickle.load(f)

# Training loop
if __name__ == '__main__':
    for level in ['easy', 'medium', 'hard']:
        ai = ConnectFourAI(level)
        for episode in range(10000 if level=='easy' else 50000):
            board = [['']*7 for _ in range(6)]
            available = [i for i in range(7)]
            moves = []
            player = 'red'
            while True:
                action = ai.choose_action(board, available)
                for row in range(5, -1, -1):
                    if board[row][action] == '':
                        board[row][action] = player
                        break
                moves.append(([[cell for cell in row] for row in board], action, available[:]))
                available = [i for i in range(7) if board[0][i] == '']
                winner = None
                # Check win
                for r in range(6):
                    for c in range(7):
                        if board[r][c] != '':
                            for dr, dc in [(0,1),(1,0),(1,1),(1,-1)]:
                                try:
                                    if all(board[r+dr*i][c+dc*i]==board[r][c] for i in range(4)):
                                        winner = board[r][c]
                                except:
                                    pass
                if winner or not available:
                    reward = 1 if winner == 'red' else -1 if winner == 'yellow' else 0
                    for b, a, av in moves:
                        ai.update(b, a, reward, b, av)
                    break
                player = 'yellow' if player == 'red' else 'red'
        ai.save(f'cf_ai_{level}.pkl')
