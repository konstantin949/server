def generate_field(n):
    a=[]
    b=[]
    for i in range(1,n**2+1):
        if i%n==0:
            b.append(i)
            a.append(b)
            b=[]
        else:
            b.append(i)
    return a

def create_win_combinations(n, d):
    a = generate_field(n)
    # d - длина выйгрышной комбинации
    win_list = []
    # цикл для горизонталей
    for i in range(len(a)):
        for j in range(len(a)):
            if len(a[i][j:(j + d)]) == d:
                win_list.append(a[i][j:(j + d)])

    # цикл для вертикалей
    help_list = []
    for i in range(len(a)):
        b = []
        for j in range(len(a)):
            b.append(a[j][i])
        help_list.append(b)

    for i in range(len(help_list)):
        for j in range(len(help_list)):
            if len(help_list[i][j:(j + d)]) == d:
                win_list.append(help_list[i][j:(j + d)])

    # цикл для диагоналей слева-направо
    for k in range(len(a)):
        help_list = []
        i = 0
        while i != (len(a) - k):
            help_list.append(a[i][i + k])
            i += 1
        win_list.append(help_list)

    for k in range(1, len(a)):
        help_list = []
        i = k
        while i <= len(a) - 1:
            help_list.append(a[i][i - k])
            i += 1
        win_list.append(help_list)

    # цикл для диагоналей справа-налево
    for k in range(len(a)):
        help_list = []
        i = k
        j = 0
        while i >= 0:
            help_list.append(a[i][j])
            i = i - 1
            j += 1
        win_list.append(help_list)

    for k in range(1, len(a)):
        help_list = []
        i = k
        j = len(a) - 1
        while i <= len(a) - 1:
            help_list.append(a[i][j])
            i += 1
            j -= 1
        win_list.append(help_list)

    # отбор нужных значений
    help_list = []
    for i in win_list:
        if len(i) < d:
            continue
        else:
            help_list.append(i)

    win_list = []

    for i in range(len(help_list)):
        for j in range(len(help_list)):
            if len(help_list[i][j:(j + d)]) == d:
                win_list.append(help_list[i][j:(j + d)])

    for i in range(len(win_list)):
        for j in range(d):
            win_list[i][j] -= 1

    return win_list

class Game:
    def __init__(self, game_id, player1_key, size_of_board, length_of_win_comb):
        self.id = game_id

        self.player1_key = player1_key
        self.player2_key = None

        self.winner = None

        self.size_of_board = size_of_board
        self.length_of_win_comb = length_of_win_comb

        self.current_move = 1

        self.board = '-' * size_of_board ** 2

        self.win_combinations = create_win_combinations(size_of_board, length_of_win_comb)

        self.count_draw=0

    def make_move(self, board):
        self.count_draw+=1
        self.board = board
        self.current_move = self.current_move % 2 + 1
        winner = self.check_winner()
        if winner == 'X' or winner == 'O':
            self.winner = winner
        elif self.check_draw():
            return 'draw'
        return winner

    def check_winner(self):
        for combination in self.win_combinations:
            winner = self.board[combination[0]]
            if winner == '-':
                continue
            for i in combination:
                if self.board[i] != winner:
                    winner = None
                    break

            if winner is not None:
                return winner

        return '-'

    def check_draw(self):
        if self.count_draw==self.size_of_board**2:
            self.winner='draw'
            return True
        else:
            return False




games = {}
