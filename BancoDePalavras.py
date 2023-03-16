import random

class BancoDePalavras():

    def __init__(self):
        self.__palavras = ['amigo', 'arvore', 'banco', 'bebida', 'bicicleta', 'casa', 'comida', 'dia', 'dinheiro',
                         'escola', 'familia', 'feira', 'festa', 'fogo', 'frio', 'gato', 'hospital', 'igreja',
                         'jardim', 'livro', 'lua', 'maquina', 'mar', 'mundo', 'noite', 'ovo', 'pao', 'pessoa',
                         'piscina', 'porta', 'prato', 'sapato', 'sol', 'terra', 'trabalho', 'vaca', 'voo', 'agua',
                         'cidade', 'coracao', 'elefante', 'futebol', 'garrafa', 'grama', 'hotel', 'iglu', 'ilha',
                         'imagem', 'janela', 'jornal', 'limao', 'limpeza', 'loja', 'mala', 'mao', 'mesa', 'montanha',
                         'navio', 'neve', 'nota', 'novo', 'olho', 'onda', 'orelha', 'ouro', 'papel', 'pato', 'peixe',
                         'piano', 'pincel', 'ponte', 'presente', 'radio', 'rio', 'robo', 'roupa', 'sala', 'sapo',
                         'telefone', 'tenis', 'tempo', 'terrao', 'texto', 'tigre', 'trem', 'uva', 'vento', 'verao',
                         'viagem', 'vida', 'vidro', 'vinho', 'yoga', 'zebra', 'zero'] #lista de palavras sem acento e sem 'ç'

    def palavra_aleatoria(self):
        return random.choice(self.__palavras)