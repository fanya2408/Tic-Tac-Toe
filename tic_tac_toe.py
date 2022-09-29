class TicTacToe:
    def __init__(self, symbol, play_with_bot):

        self.play_with_bot = play_with_bot
        self.game_board = self.create_playboard()
        self.symbol_1, self.symbol_2 = self.assign_symbols_to_users(symbol)
        self.count = 0
        self.winner = False

    def create_playboard(self):
        board = []

        for row in range(3):
            board.append([])
            for column in range(3):
                board[-1].append('')

        return board

    def assign_symbols_to_users(self, symbol):
        symbol_1 = symbol.upper()

        if symbol_1 == 'X':
            symbol_2 = 'O'
            # print("Player 2, you are O.")
            return symbol_1, symbol_2

        if symbol_1 == 'O':
            symbol_2 = 'X'
            # print("Player 2, you are X.")
            return symbol_1, symbol_2

    def make_turn(self, inp_row, inp_column):

        if self.count % 2 == 0:
            player = self.symbol_1
        else:
            player = self.symbol_2
        # print(f'Player {player}, it is your turn.')

        if (inp_row < 0 or inp_row > 2) or (inp_column < 0 or inp_column > 2):
            return False

        if (self.game_board[inp_row][inp_column] == self.symbol_1) or \
                (self.game_board[inp_row][inp_column] == self.symbol_2):
            return False

        if player == self.symbol_1:
            self.game_board[inp_row][inp_column] = self.symbol_1
        else:
            self.game_board[inp_row][inp_column] = self.symbol_2
        self.count += 1

        self.find_winner()

        if self.play_with_bot and not self.winner and not self.check_tie():
            bot_turn_x, bot_turn_y = self.bot_make_turn()

            self.game_board[bot_turn_x][bot_turn_y] = self.symbol_2
            self.count += 1

            self.find_winner()

        return True

    def bot_make_turn(self):

        if self.game_board[0][0] == self.game_board[0][1] == self.symbol_1 and self.game_board[0][2] == '':
            return 0, 2
        elif self.game_board[0][1] == self.game_board[0][2] == self.symbol_1 and self.game_board[0][0] == '':
            return 0, 0
        elif self.game_board[0][0] == self.game_board[0][2] == self.symbol_1 and self.game_board[0][1] == '':
            return 0, 1
        elif self.game_board[1][0] == self.game_board[1][1] == self.symbol_1 and self.game_board[1][2] == '':
            return 1, 2
        elif self.game_board[1][1] == self.game_board[1][2] == self.symbol_1 and self.game_board[1][0] == '':
            return 1, 0
        elif self.game_board[1][0] == self.game_board[1][2] == self.symbol_1 and self.game_board[1][1] == '':
            return 1, 1
        elif self.game_board[2][0] == self.game_board[2][1] == self.symbol_1 and self.game_board[2][2] == '':
            return 2, 2
        elif self.game_board[2][1] == self.game_board[2][2] == self.symbol_1 and self.game_board[2][0] == '':
            return 2, 0
        elif self.game_board[2][0] == self.game_board[2][2] == self.symbol_1 and self.game_board[2][1] == '':
            return 2, 1
        # do not let the X win in a row

        elif self.game_board[0][0] == self.game_board[1][0] == self.symbol_1 and self.game_board[2][0] == '':
            return 2, 0
        elif self.game_board[1][0] == self.game_board[2][0] == self.symbol_1 and self.game_board[0][0] == '':
            return 0, 0
        elif self.game_board[0][0] == self.game_board[2][0] == self.symbol_1 and self.game_board[1][0] == '':
            return 1, 0
        elif self.game_board[0][1] == self.game_board[1][1] == self.symbol_1 and self.game_board[2][1] == '':
            return 2, 1
        elif self.game_board[1][1] == self.game_board[2][1] == self.symbol_1 and self.game_board[0][1] == '':
            return 0, 1
        elif self.game_board[0][1] == self.game_board[2][1] == self.symbol_1 and self.game_board[1][1] == '':
            return 1, 1
        elif self.game_board[0][2] == self.game_board[1][2] == self.symbol_1 and self.game_board[2][2] == '':
            return 2, 2
        elif self.game_board[1][2] == self.game_board[2][2] == self.symbol_1 and self.game_board[0][2] == '':
            return 0, 2
        elif self.game_board[0][2] == self.game_board[2][2] == self.symbol_1 and self.game_board[1][2] == '':
            return 1, 2
        # do not let the X win in a column

        elif self.game_board[0][0] == self.game_board[1][1] == self.symbol_1 and self.game_board[2][2] == '':
            return 2, 2
        elif self.game_board[2][2] == self.game_board[1][1] == self.symbol_1 and self.game_board[0][0] == '':
            return 0, 0
        elif self.game_board[0][0] == self.game_board[2][2] == self.symbol_1 and self.game_board[1][1] == '':
            return 1, 1
        elif self.game_board[2][0] == self.game_board[1][1] == self.symbol_1 and self.game_board[0][2] == '':
            return 0, 2
        elif self.game_board[1][1] == self.game_board[0][2] == self.symbol_1 and self.game_board[2][0] == '':
            return 2, 0
        elif self.game_board[2][0] == self.game_board[0][2] == self.symbol_1 and self.game_board[1][1] == '':
            return 1, 1
        # do not let the X win in a diagonal

        elif self.game_board[1][1] == '':
            return 1, 1
        elif self.game_board[1][0] == '':
            return 1, 0
        elif self.game_board[1][2] == '':
            return 1, 2
        elif self.game_board[0][2] == '':
            return 0, 2
        elif self.game_board[0][1] == '':
            return 0, 1
        elif self.game_board[0][0] == '':
            return 0, 0
        elif self.game_board[2][0] == '':
            return 2, 0
        elif self.game_board[2][1] == '':
            return 2, 1

    def find_winner(self):

        for column in range(3):
            if self.game_board[0][column] == self.game_board[1][column] == self.game_board[2][column] == self.symbol_1:
                self.winner = True
            elif self.game_board[0][column] == self.game_board[1][column] == self.game_board[2][column] == self.symbol_2:
                self.winner = True

        for row in range(3):
            if self.game_board[row][0] == self.game_board[row][1] == self.game_board[row][2] == self.symbol_1:
                self.winner = True
            elif self.game_board[row][0] == self.game_board[row][1] == self.game_board[row][2] == self.symbol_2:
                self.winner = True

        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == self.symbol_1:
            self.winner = True
        elif self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == self.symbol_2:
            self.winner = True
        elif self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] == self.symbol_1:
            self.winner = True
        elif self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] == self.symbol_2:
            self.winner = True

        return self.winner

    def check_tie(self):

        for row in self.game_board:
            for element in row:
                if element == '':
                    return False

        return True

    def result_win(self):

        if self.winner is True and self.count % 2 == 1:
            return f'{self.symbol_1} won!'
        elif self.winner is True and self.count % 2 == 0:
            return f'{self.symbol_2} won!'

        return None


if __name__ == '__main__':
    inp_symbol = input('Player 1, do you want to be X or O? ')

    play_with_bot = input('Do you wanna play with a computer? Please, answer "yes" or "no".')
    play_with_bot = play_with_bot == 'yes'

    tic_tac = TicTacToe(inp_symbol, play_with_bot)

    while tic_tac.count < 10 and tic_tac.winner is False:
        print(tic_tac.game_board)
        step_finished = False
        while not step_finished:

            inp_row = int(input('Choose a row! '
                                'To choose upper row: enter 0, middle row: enter 1, bottom row: enter 2.'))
            inp_column = int(input('Choose a column! '
                                   'To choose left column: enter 0, middle column: enter 1, right column enter 2.'))

            step_finished = tic_tac.make_turn(inp_row, inp_column)

            if (tic_tac.count == 9) and (tic_tac.winner is False):
                print('The tie!')
                tic_tac.result_win()
                tic_tac.count += 1

            if (tic_tac.count == 9) and (tic_tac.winner is True):
                print('Game over!')

    if tic_tac.winner is True:
        tic_tac.result_win()
