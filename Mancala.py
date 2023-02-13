# Author: Evelyn Aron
# GitHub username: Evs96
# Date: 12/2/2022
# Description: This program contains a Player class, that's main function is to create a player object and retrieve the
#              name of the player object. This program contains another class named Mancala. This class contains the
#              following methods: create_player,print_board, return_winner, and play_game. The Mancala class essentially
#              contains information about the two players and information about the Mancala board to play a text-based
#              version of the game.

class Player:
    """A class to represent a player with a name. Used by the Mancala class in the return_winner method to return
       the name of the winner and in the create_player method to create a player object.
     """

    def __init__(self, name):
        """Creates a player object with a specified name. Takes a name as its parameter. Initializes the data
           member as private.
         """

        self._name = name

    def get_name(self):
        """Returns the name. Used by the Mancala class in the return_winner method to return the name of the winner."""

        return self._name


class Mancala:
    """Represents a Mancala game, played by two players. """

    def __init__(self):
        """Creates a Mancala game object. Takes no parameters. Initializes the components of a Mancala game. All
           data members are private.
         """

        self._game_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self._player_1 = None
        self._player_2 = None
        self._game_winner = None
        self._game_tie = None
        self._player_1_pits = None
        self._player_2_pits = None
        self._player_1_store = None
        self._player_2_store = None

    def create_player(self, player_name):
        """Takes player_name as its parameter. Returns the player object using the Player class. """

        if self._player_1 is None:
            self._player_1 = Player(player_name)
        else:
            self._player_2 = Player(player_name)

    def print_board(self):
        """Takes no parameters. Prints current board information: player1/player2, store and seeds for respective
           player.
        """

        print("player1:")
        print("store: " + str(self._player_1_store))
        print(self._player_1_pits)
        print("player2:")
        print("store: " + str(self._player_2_store))
        print(self._player_2_pits)

    def return_winner(self):
        """Takes no parameters. Returns the winner, specifying if the winner is player one or player two as well
           as their respective names. If the game is a tie, then returns "It's a tie". Finally, if the game has
           not ended(meaning there is no winner yet), returns "Game has not ended" .
        """

        if self._game_winner == self._player_1:
            return "Winner is player 1: " + self._player_1.get_name()
        if self._game_winner == self._player_2:
            return "Winner is player 2: " + self._player_2.get_name()
        if self._game_tie is True:
            return "It's a tie"
        if self._game_winner is None:
            return "Game has not ended"

    def play_game(self, player_index, pit_index):
        """Takes two parameters, the player index (1/2) and the pit index(1-6). Checks if the pit_index is within
           the allowed range [1-6], inclusive, if it is not then it returns "Invalid number for pit index".
           If there is a winner then returns "game has ended". During their turn, if player 1/2's last seed
           lands in their store then "player (1/2) take another turn" is printed. During their turn, if player
           1/2's last seed lands on their pit that was previously empty then all the seeds on the opponents
           pit that corresponds(exactly opposite) with the current pit goes to the current player's store
           along with the last seed that landed on the empty pit. When all of one player's pits are
           empty, the game is over and the opponent takes the remaining seeds in their pits and stores
           them in their store, whoever has the most seeds wins and self._game_winner is self._player_1 or
           self._player_2. If the game is a tie then self._tie is True. The player's pits and stores are
           updated throughout.
        """

        if pit_index > 6 or pit_index <= 0:
            return "Invalid number for pit index"
        if self._game_winner is not None:
            return "Game is ended"

        if player_index == 1:
            new_pit_index = pit_index - 1
            number = self._game_board[new_pit_index]
            self._game_board[new_pit_index] = 0

            for num in range(0, number):
                new_pit_index += 1
                if new_pit_index >= 13:
                    new_pit_index = 0

                if new_pit_index != 13:
                    self._game_board[new_pit_index] += 1

                if num == number - 1 and new_pit_index == 6:
                    print("player 1 take another turn")

                if num == number - 1 and self._game_board[new_pit_index] == 1 and new_pit_index == 5:
                    if self._game_board[5] == 1:
                        quant = self._game_board[7]
                        self._game_board[7] = 0
                        self._game_board[5] = 0
                        total = quant + 1
                        self._game_board[6] += total

                if num == number - 1 and self._game_board[new_pit_index] == 1 and new_pit_index == 4:
                    if self._game_board[4] == 1:
                        quant = self._game_board[8]
                        self._game_board[8] = 0
                        self._game_board[4] = 0
                        total = quant + 1
                        self._game_board[6] += total

                if num == number - 1 and self._game_board[new_pit_index] == 1 and new_pit_index == 3:
                    if self._game_board[3] == 1:
                        quant = self._game_board[9]
                        self._game_board[9] = 0
                        self._game_board[3] = 0
                        total = quant + 1
                        self._game_board[6] += total

                if num == number - 1 and self._game_board[new_pit_index] == 1 and new_pit_index == 2:
                    if self._game_board[2] == 1:
                        quant = self._game_board[10]
                        self._game_board[10] = 0
                        self._game_board[2] = 0
                        total = quant + 1
                        self._game_board[6] += total

                if num == number - 1 and self._game_board[new_pit_index] == 1 and new_pit_index == 1:
                    if self._game_board[1] == 1:
                        quant = self._game_board[11]
                        self._game_board[11] = 0
                        self._game_board[1] = 0
                        total = quant + 1
                        self._game_board[6] += total

                if num == number - 1 and self._game_board[new_pit_index] == 1 and new_pit_index == 0:
                    if self._game_board[0] == 1:
                        quant = self._game_board[12]
                        self._game_board[12] = 0
                        self._game_board[0] = 0
                        total = quant + 1
                        self._game_board[6] += total

            self._player_1_pits = self._game_board[0:6]
            self._player_2_pits = self._game_board[7:13]
            self._player_1_store = self._game_board[6]
            self._player_2_store = self._game_board[13]

            if self._game_board[0:6] == [0, 0, 0, 0, 0, 0]:
                remaining = self._game_board[7] + self._game_board[8] + self._game_board[9] + self._game_board[10] + \
                            self._game_board[11] + self._game_board[12]
                self._game_board[7] = 0
                self._game_board[8] = 0
                self._game_board[9] = 0
                self._game_board[10] = 0
                self._game_board[11] = 0
                self._game_board[12] = 0
                self._game_board[13] += remaining

                if self._game_board[6] > self._game_board[13]:
                    self._game_winner = self._player_1
                if self._game_board[6] < self._game_board[13]:
                    self._game_winner = self._player_2
                if self._game_board[6] == self._game_board[13]:
                    self._game_tie = True
                self._player_1_pits = self._game_board[0:6]
                self._player_2_pits = self._game_board[7:13]
                self._player_1_store = self._game_board[6]
                self._player_2_store = self._game_board[13]

            return self._game_board

        if player_index == 2:
            new_pit_index_2 = pit_index + 6
            number = self._game_board[new_pit_index_2]
            self._game_board[new_pit_index_2] = 0

            for num in range(0, number):
                new_pit_index_2 += 1
                if new_pit_index_2 > 13:
                    new_pit_index_2 = 0

                elif new_pit_index_2 == 6:
                    new_pit_index_2 += 1

                if new_pit_index_2 != 6:
                    self._game_board[new_pit_index_2] += 1

                if num == number - 1 and new_pit_index_2 == 13:
                    print("player 2 take another turn")

                if num == number - 1 and self._game_board[new_pit_index_2] == 1 and new_pit_index_2 == 7:
                    if self._game_board[7] == 1:
                        quant = self._game_board[5]
                        self._game_board[5] = 0
                        self._game_board[7] = 0
                        total = quant + 1
                        self._game_board[13] += total

                if num == number - 1 and self._game_board[new_pit_index_2] == 1 and new_pit_index_2 == 8:
                    if self._game_board[8] == 1:
                        quant = self._game_board[4]
                        self._game_board[4] = 0
                        self._game_board[8] = 0
                        total = quant + 1
                        self._game_board[13] += total

                if num == number - 1 and self._game_board[new_pit_index_2] == 1 and new_pit_index_2 == 9:
                    if self._game_board[9] == 1:
                        quant = self._game_board[3]
                        self._game_board[3] = 0
                        self._game_board[9] = 0
                        total = quant + 1
                        self._game_board[13] += total

                if num == number - 1 and self._game_board[new_pit_index_2] == 1 and new_pit_index_2 == 10:
                    if self._game_board[10] == 1:
                        quant = self._game_board[2]
                        self._game_board[2] = 0
                        self._game_board[10] = 0
                        total = quant + 1
                        self._game_board[13] += total

                if num == number - 1 and self._game_board[new_pit_index_2] == 1 and new_pit_index_2 == 11:
                    if self._game_board[11] == 1:
                        quant = self._game_board[1]
                        self._game_board[1] = 0
                        self._game_board[11] = 0
                        total = quant + 1
                        self._game_board[13] += total

                if num == number - 1 and self._game_board[new_pit_index_2] == 1 and new_pit_index_2 == 12:
                    if self._game_board[12] == 1:
                        quant = self._game_board[0]
                        self._game_board[0] = 0
                        self._game_board[12] = 0
                        total = quant + 1
                        self._game_board[13] += total

            self._player_2_pits = self._game_board[7:13]
            self._player_1_pits = self._game_board[0:6]
            self._player_1_store = self._game_board[6]
            self._player_2_store = self._game_board[13]

            if self._game_board[7:13] == [0, 0, 0, 0, 0, 0]:
                remaining = self._game_board[0] + self._game_board[1] + self._game_board[2] + self._game_board[3] + \
                            self._game_board[4] + self._game_board[5]
                self._game_board[0] = 0
                self._game_board[1] = 0
                self._game_board[2] = 0
                self._game_board[3] = 0
                self._game_board[4] = 0
                self._game_board[5] = 0
                self._game_board[6] += remaining

                if self._game_board[6] > self._game_board[13]:
                    self._game_winner = self._player_1
                if self._game_board[6] < self._game_board[13]:
                    self._game_winner = self._player_2
                if self._game_board[6] == self._game_board[13]:
                    self._game_tie = True

                self._player_2_pits = self._game_board[7:13]
                self._player_1_pits = self._game_board[0:6]
                self._player_1_store = self._game_board[6]
                self._player_2_store = self._game_board[13]

            return self._game_board

# game = Mancala()
# game.create_player("Evelyn")
# game.create_player("Amorette")
# print(game._game_board)
# print(game.play_game(1, 1))
# print(game.play_game(1, 2))
# print(game.play_game(1, 3))
# print(game.play_game(1, 4))
# print(game.play_game(1, 5))
# print(game.play_game(1, 6))
# print(game.play_game(1, 6))
# print(game.return_winner())
# game.print_board()
#
# game = Mancala()
# player1 = game.create_player("Lily")
# player2 = game.create_player("Lucy")
# print(game.play_game(1, 3))
# game.play_game(1, 1)
# game.play_game(2, 3)
# game.play_game(2, 4)
# game.play_game(1, 2)
# game.play_game(2, 2)
# game.play_game(1, 1)
# game.print_board()
# print(game.return_winner())
#
# game = Mancala()
# player1 = game.create_player("Lily")
# player2 = game.create_player("Lucy")
# game.play_game(1, 1)
# game.play_game(1, 2)
# game.play_game(1, 3)
# game.play_game(1, 4)
# game.play_game(1, 5)
# game.play_game(1, 6)
# game.print_board()
# print(game.return_winner())

# game = Mancala()
# player1 = game.create_player("Lily")
# player2 = game.create_player("Lucy")
# game.play_game(1,3)
# game.play_game(1,4)
# game.play_game(2,2)
# game.play_game(2,3)
# print(game.play_game(1,5))
# print(game.play_game(2,2))
# print(game.play_game(1,6))
# print(game.play_game(2,4))
# game.play_game(1,5)
# game.play_game(2,2)
# game.play_game(1,2)
# game.play_game(1,1)
# game.play_game(1,5)
# print(game.play_game(1,4))
# game.play_game(1,6)
# game.play_game(2,1)
# game.play_game(1,3)
# game.play_game(2,2)
# game.play_game(1,5)
# game.play_game(1,6)
# game.play_game(1,4)
# print(game.play_game(2,3))
# print(game.play_game(1,2))
# print(game.play_game(2,5))
# game.play_game(1,5)
# game.play_game(2,4)
# game.play_game(1,4)
# game.play_game(2,6)
# print(game.play_game(1,6))
# print(game.play_game(1,5))
# print(game.play_game(2,2))
# game.print_board()