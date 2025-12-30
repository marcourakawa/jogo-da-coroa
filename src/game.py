from board import Board
from player import Player
import time
import random as rd

class Game:
    """
    Classe responsávl por controlar o jogo.
    Ela conecta o tabuleiro (Board) com os jogadores (Player)
    e gerencia a partida
    """
    
    def __init__(self):
        """
        Construtor da classe Game.
        Executado automáticamente quando o jog0 começa.
        """

        self.board = Board()
        self.player1 = Player("Jogador 1", "O")
        self.player2 = Player("Jogador 2", "X")

        self.current_player = self.player1

    def switch_player(self):
        """
        Alterna o jogador atual.
        Se for o jogador 1, muda para o jogador 2.
        Se for o jogador 2, muda para o jogador 1.
        """

        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def play(self):
        """
        Método principal do jogo.
        Controla o loop do jogo, jogadas, vitórias e empate.
        """

        print("JOGO")
        time.sleep(1)
        print("DA")
        time.sleep(1)
        print("COROA")

        while True:

            self.board.show()

            move = self.current_player.make_move()

            if self.board.make_move(move, self.current_player.symbol):

                if self.board.check_winner(self.current_player.symbol):
                    self.board.show()
                    print(f"{self.current_player.name} Venceu!")
                    break
            
                if self.board.is_full():
                    self.board.show()
                    print("Empate!")
                    break

                self.switch_player()
            
            else:
                print("Posição ocupada. Tente novamente.")
                