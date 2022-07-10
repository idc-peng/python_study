class Tictactoe:
    casetowin = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def __init__(self):
        self.board = list(range(1, 10))
        self.available = list(range(1, 10))
        self.winner = 0
        self.phase = 1

    def __str__(self):
        string = ''
        for i in range(3):
            row = self.board[i * 3:i * 3 + 3]
            string += '\t\t*\t\t*\t\n\t{0[0]}\t*\t{0[1]}\t*\t{0[2]}\n\t\t*\t\t*\t\n'.format(row)
        return string

    def move(self, x):
        self.board[x - 1] = 'O' if self.phase == 1 else 'X'
        self.available.remove(x)
        self.winner = self.checkcase()
        self.phase = 2 if self.phase == 1 else 1

    def checkcase(self):
        caselist = []
        for case in self.casetowin:
            caselist = [self.board[x] for x in case]
            if caselist.count('O') == 3:
                return 1
            elif caselist.count('X') == 3:
                return 2
            else:
                continue
        return 0


if __name__ == '__main__':
    t = Tictactoe()

    while t.winner == 0 and len(t.available) != 0:
        move = 0
        print('\n' + str(t))
        string = 'Player {0} - Please type a position (available position(s) are {1}): ' \
            .format(t.phase, ','.join([str(x) for x in t.available]))
        while move not in t.available:
            try:
                move = int(input(string))
                if move not in t.available: raise TypeError
            except:
                print('Please try again. ', end='')
        t.move(move)

    else:
        print(t)
        if t.winner > 0:
            print('The winner is: Player ' + str(t.winner))
        else:
            print('The game ended up in a tie')