import random
import pickle

# Simple Q-learning for Tic-Tac-Toe
class TicTacToeAI:
    def __init__(self, level='easy'):
        self.q = {}
        self.level = level
        self.epsilon = {'easy': 0.8, 'medium': 0.3, 'hard': 0.05}[level]
        self.alpha = 0.5
        self.gamma = 0.9

    def get_state(self, board):
        return tuple(board)

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
        ai = TicTacToeAI(level)
        for episode in range(10000 if level=='easy' else 50000):
            board = ['']*9
            available = list(range(9))
            moves = []
            player = 'X'
            while True:
                action = ai.choose_action(board, available)
                board[action] = player
                moves.append((board[:], action, available[:]))
                available.remove(action)
                winner = None
                for line in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
                    if board[line[0]] == board[line[1]] == board[line[2]] != '':
                        winner = board[line[0]]
                if winner or not available:
                    reward = 1 if winner == 'X' else -1 if winner == 'O' else 0
                    for b, a, av in moves:
                        ai.update(b, a, reward, b, av)
                    break
                player = 'O' if player == 'X' else 'X'
        ai.save(f'ttt_ai_{level}.pkl')
