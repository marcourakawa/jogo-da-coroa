class Player:
    """
    Classe que representa um jogador do jogo da coroa
    Resposável por armazenar:
    - nome do corno
    - símbolo do jogador
    - ação de escolher uma jogada
    """

    def __init__(self, name, symbol):
        """
        Contrutor da classe Player

        :param name: Nome do jogador (ex: "Jogador 1")
        :param symbol: Símbolo usado no tabuleiro ('X' ou 'O')
        """

        self.name = name
        self.symbol = symbol

    def make_move(self):
        """
        Método responsável por pedir ao jogador a posição
        onde ele deseja jogar.

        Retorna:
            Um número entre 0 e 8
        """

        while True:
            try:
                print(f"{self.name} ({self.symbol}), escolha uma posição (0 a 8): ")
                move = int(input())

                if 0 <= move <= 8:
                    return move

                print("Posição inválida. Escolha um número entre 0 e 8.")
            
            except ValueError:
                print("Digite um número válido.")