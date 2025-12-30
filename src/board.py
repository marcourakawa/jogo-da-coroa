class Board:
    def __init__(self):

        self.positions = [" " for _ in range(9)]

    def show(self):
        """
        Exibe o tabuleiro no teminal
        """
        print()

        for i in range(0, 9, 3):

            print(
                self.positions[i] + " | " +
                self.positions[i + 1] + " | " +
                self.positions[i + 2]
            )
    
        print()

    def make_move(self, position, symbol):
        """
        Realiza uma jogada no tabuleiro.

        :param position: posição escolhida (0 a 8)
        :param symbol: símbolo do jogador ('X' ou 'O')
        :return: True se a jogada for válida, False caso contrário
        """

        # Verifica se a posição está vazia
        if self.positions[position] == " ":
            self.positions[position] = symbol
            return True
        return False

    def check_winner(self, symbol):
        """
        Verifica e o jogador atual venceu.

        :param symbol: símbolo do jogador ('X' ou 'O')
        :return: True se venceu, False caso contrário
        """

        wins = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],

            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],

            [0, 4, 8],
            [2, 4, 6]
        ]

        return any(
            all(self.positions[i] == symbol for i in combo)
            for combo in wins
        )

    def is_full(self):
        """
        Verifica se o tabuleiro está cheio.

        :return: True se não houver mais espações vazios
        """

        return " " not in self.positions
        