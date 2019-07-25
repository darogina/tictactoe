#!/usr/bin/env python
"""
Written by  : David Rogina - github.com/darogina
Description : A friendly game of Tic-Tac-Toe with a twist... You can't win!
            The game is set up such that the computer will always win or force a draw.
            This script is fully compatible with both python 2 & 3
"""

import random
import signal
import sys


def signal_handler(sig, frame):
    print('')
    print('Goodbye!!')
    # sys.exit(0)
    sys.exit(sig)


def backwards_compatible():
    # Quick an dirty way of adding backwards compatibility. Ideally a better solution would be put in place like
    # futures but this will make it so no extra packages need to be installed
    try:
        global input
        input = raw_input
    except NameError:
        pass


class TicTacToe:
    """
    Tic-Tac-Toe game where you can never win.
    The game is set up so that the computer will always win or force a draw.
    """
    _corners = [1, 3, 7, 9]
    _sides = [2, 4, 6, 8]
    _center = 5
    _winning_combos = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # vertical
        (1, 5, 9), (3, 5, 7)  # diagonal
    ]

    def __init__(self):
        # Initialize the board
        self._board = [''] * 9
        self.computer_icon = 'X'
        self.player_icon = 'O'
        self.move_counter = 0
        self.game_complete = False

    def __make_move(self, cell, icon):
        self._board[cell - 1] = icon
        return cell

    def __move_center(self, icon):
        return self.__make_move(self._center, icon)

    def __move_side(self, icon):
        for i in self._sides:
            if self.is_available(i):
                return self.__make_move(i, icon)

    def __prompt_player(self):
        cell = -1
        while cell not in range(1, 10):
            try:
                cell = int(input("Select a free cell between (1 - 9): "))
            except ValueError:
                print("Invalid selection!")
                continue
        return cell

    def __move_computer(self):
        # Complete all the necessary steps to move the player
        if not self.is_move_possible():
            return

        move = -1
        try:
            # Check if the computer can win this turn
            result = self.is_win_possible(self.computer_icon)
            if result[0]:
                # Win possible. Make appropriate move
                move = self.__make_move(result[1], self.computer_icon)
                self.game_complete = True
                return

            # Check if player can win on their next turn
            result = self.is_win_possible(self.player_icon)
            if result[0]:
                # Win possible. Block the player
                move = self.__make_move(result[1], self.computer_icon)
                return

            # If the player went first then the first two moves by the computer must be specific in order to
            # guarantee that it doesn't lose
            if self.move_counter == 1 \
                    and [self._board[idx - 1] for idx in self._corners].count(self.player_icon) >= 1:
                # First move and player took a corner.
                # Take the center
                move = self.__move_center(self.computer_icon)
                return
            elif self.move_counter == 3 and [self._board[idx - 1] for idx in self._corners].count(
                    self.player_icon) >= 2:
                # Second move and player controls two corners
                # Take one of the sides
                move = self.__move_side(self.computer_icon)
                return

            # Take corner if available
            for i in self._corners:
                # The 'i - 2' in the case of i == 1 will be a negative look back.
                if self.is_available(i) and self._board[i - 2] != self.player_icon:
                    move = self.__make_move(i, self.computer_icon)
                    return

            # Take center if available
            if self.is_available(self._center):
                move = self.__move_center(self.computer_icon)
                return

            # Take side if available
            move = self.__move_side(self.computer_icon)

        finally:
            self.move_counter += 1
            print("Computer moved to cell %s" % move)

    def __move_player(self):
        # Complete all the necessary steps to move the player
        if not self.is_move_possible():
            return

        try:
            cell = self.__prompt_player()
            while not self.is_available(cell):
                print("The selected cell is already used!")
                cell = self.__prompt_player()

            self._board[cell - 1] = self.player_icon
        finally:
            self.move_counter += 1

    def start(self):
        # Start the game
        self.__init__()

        print("The computer is %c's and you are %c's" % (self.computer_icon, self.player_icon))
        print('')

        # Randomly pick who will go first. Computer is 0, player is 1
        turn = random.randint(0, 1)
        if turn == 0:
            print('The computer will go first')
        else:
            print('You will go first')

        # Print the initial board
        self.print_board()

        while not self.game_complete:
            if self.move_counter % 2 == turn:
                # Computers Turn
                self.__move_computer()
                # self.print_board()
            else:
                # Players Turn
                self.__move_player()
                # self.print_board()

            # Print the board after turn
            self.print_board()

        if self.is_winner(self.computer_icon):
            print("Computer Wins!!")
        elif self.is_winner(self.player_icon):
            print("You Win!!")
        else:
            print("Draw!!")

    def print_board(self):
        # Print the current state of the board
        print('')
        print(" %s | %s | %s " % (self._board[0] or 1, self._board[1] or 2, self._board[2] or 3))
        print('-----------')
        print(" %s | %s | %s " % (self._board[3] or 4, self._board[4] or 5, self._board[5] or 6))
        print('-----------')
        print(" %s | %s | %s " % (self._board[6] or 7, self._board[7] or 8, self._board[8] or 9))
        print('')

    def is_move_possible(self):
        # Check if any moves are possible
        if self.move_counter == 9:
            print("No more moves available!")
            self.game_complete = True
            return False

        return True

    def is_available(self, cell):
        # Check if the cell is available
        return 0 < cell < 10 and not self._board[cell - 1]

    def is_win_possible(self, icon):
        # Check if a win is possible this turn
        for combo in self._winning_combos:
            sublist = [self._board[idx - 1] for idx in combo]
            if sublist.count(icon) == 2 and sublist.count(''):
                # A winning move exists
                return True, combo[sublist.index('')]

        return False, -1

    def is_winner(self, icon):
        # Check if winner
        for combo in self._winning_combos:
            sublist = [self._board[idx - 1] for idx in combo]
            if sublist.count(icon) == 3:
                # Winner
                self.game_draw = False
                self.game_complete = True
                return True

        return False


def main():
    # Register signal handler
    signal.signal(signal.SIGINT, signal_handler)

    # Fix input so it works with python2
    backwards_compatible()

    game = TicTacToe()
    play_game = True
    while play_game:
        game.start()
        if not str(input("Do you want to play again? y or n : ")).lower().startswith('y'):
            play_game = False

    print("Goodbye!!")


if __name__ == '__main__':
    main()
