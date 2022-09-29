from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

from tic_tac_toe import TicTacToe

Form, Window = uic.loadUiType("./ui/xoxo.ui")


class MainWindow(Window):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tic-Tac-Toe")


class MainForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.tic_tac = TicTacToe('X', None)

    def setupUi(self, *args):
        super().setupUi(*args)

        self.button_top_left.clicked.connect(self.button_top_left_action)
        self.button_top_mid.clicked.connect(self.button_top_mid_action)
        self.button_top_right.clicked.connect(self.button_top_right_action)
        self.button_mid_left.clicked.connect(self.button_mid_left_action)
        self.button_mid_mid.clicked.connect(self.button_mid_mid_action)
        self.button_mid_right.clicked.connect(self.button_mid_right_action)
        self.button_bot_left.clicked.connect(self.button_bot_left_action)
        self.button_bot_mid.clicked.connect(self.button_bot_mid_action)
        self.button_bot_right.clicked.connect(self.button_bot_right_action)

        self.button_restart.clicked.connect(self.button_restart_action)

        self.button_bot_player.clicked.connect(self.button_bot_player_action)

        self.buttons_list = [self.button_bot_right, self.button_bot_mid, self.button_bot_left, self.button_mid_right,
                             self.button_mid_mid, self.button_mid_left, self.button_top_right, self.button_top_mid,
                             self.button_top_left]

    def finding_winner(self):
        result_win = self.tic_tac.result_win()
        check_tie = self.tic_tac.check_tie()

        if result_win is not None:
            self.label.setText(result_win)

            for button in self.buttons_list:
                if self.tic_tac.winner is True:
                    button.setEnabled(False)

        elif check_tie:
            self.label.setText("It's a tie!")

            for button in self.buttons_list:
                if self.tic_tac.winner is True:
                    button.setEnabled(False)

    def button_bot_right_action(self):
        self.tic_tac.make_turn(2, 2)
        self.update_game_board()

        self.finding_winner()

    def button_bot_mid_action(self):
        self.tic_tac.make_turn(2, 1)
        self.update_game_board()

        self.finding_winner()

    def button_bot_left_action(self):
        self.tic_tac.make_turn(2, 0)
        self.update_game_board()

        self.finding_winner()

    def button_mid_right_action(self):
        self.tic_tac.make_turn(1, 2)
        self.update_game_board()

        self.finding_winner()

    def button_mid_mid_action(self):
        self.tic_tac.make_turn(1, 1)
        self.update_game_board()

        self.finding_winner()

    def button_mid_left_action(self):
        self.tic_tac.make_turn(1, 0)
        self.update_game_board()

        self.finding_winner()

    def button_top_right_action(self):
        self.tic_tac.make_turn(0, 2)
        self.update_game_board()

        self.finding_winner()

    def button_top_mid_action(self):
        self.tic_tac.make_turn(0, 1)
        self.update_game_board()

        self.finding_winner()

    def button_top_left_action(self):
        self.tic_tac.make_turn(0, 0)
        self.update_game_board()

        self.finding_winner()

    def button_restart_action(self):

        self.tic_tac.count = 0
        self.tic_tac.winner = False
        self.tic_tac.game_board = self.tic_tac.create_playboard()

        for button in self.buttons_list:
            button.setEnabled(True)
            button.setText('')

        self.button_bot_player.setEnabled(True)
        self.label.setText('Who will win?')

    def update_game_board(self):
        self.button_top_left.setText(self.tic_tac.game_board[0][0])
        self.button_top_mid.setText(self.tic_tac.game_board[0][1])
        self.button_top_right.setText(self.tic_tac.game_board[0][2])

        self.button_mid_left.setText(self.tic_tac.game_board[1][0])
        self.button_mid_mid.setText(self.tic_tac.game_board[1][1])
        self.button_mid_right.setText(self.tic_tac.game_board[1][2])

        self.button_bot_left.setText(self.tic_tac.game_board[2][0])
        self.button_bot_mid.setText(self.tic_tac.game_board[2][1])
        self.button_bot_right.setText(self.tic_tac.game_board[2][2])

        for button in self.buttons_list:
            if button.text() != '':
                button.setEnabled(False)

    def button_bot_player_action(self):
        self.button_restart_action()
        self.tic_tac.play_with_bot = True


app = QApplication([])
window = MainWindow()
form = MainForm()
form.setupUi(window)
window.show()
app.exec()
