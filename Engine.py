import random

class Engine():
    def palavra(self):
        self.palavras = ['amigo', 'arvore', 'banco', 'bebida', 'bicicleta', 'casa', 'comida', 'dia', 'dinheiro', 'escola', 'familia', 'feira', 'festa', 'fogo', 'frio', 'gato', 'hospital', 'igreja', 'jardim', 'livro', 'lua', 'maquina', 'mar', 'mundo', 'noite', 'ovo', 'pao', 'pessoa', 'piscina', 'porta', 'prato', 'sapato', 'sol', 'terra', 'trabalho', 'vaca', 'voo', 'agua', 'cidade', 'coracao', 'elefante', 'futebol', 'garrafa', 'grama', 'hotel', 'iglu', 'ilha', 'imagem', 'janela', 'jornal', 'limao', 'limpeza', 'loja', 'mala', 'mao', 'mesa', 'montanha', 'navio', 'neve', 'nota', 'novo', 'olho', 'onda', 'orelha', 'ouro', 'papel', 'pato', 'peixe', 'piano', 'pincel', 'ponte', 'presente', 'radio', 'rio', 'robo', 'roupa', 'sala', 'sapo', 'telefone', 'tenis', 'tempo', 'terrao', 'texto', 'tigre', 'trem', 'uva', 'vento', 'verao', 'viagem', 'vida', 'vidro', 'vinho', 'yoga', 'zebra', 'zero'] #lista de palavras sem acento e sem 'ç'

    def palavra_aleatoria(self):
        return random.choice(self.palavras) #sorteia aleatoriamente uma das palavras da lista 

    
    def __init__(self, letra: str()):
        self.__acertou = bool()
        self.__repetida = bool()
        self.__letra = letra
        
    '''
    Verifica se a letra já foi utilizada, e se a letra está contida na palavra ou não.
    
    Obs: Se a letra estiver repetida a função de verificação não verifica se letra
         está ou não na palavra atual, ela apenas altera o atributo "self.__repetida"
         para "True", e por padrão se apenas classificamos uma variável como boolena
         em python(como no __init__ dessa classe) ela tem valor base "False", logo
         deve-se ter cuidado para checar se a letra está repetida ou não antes
         de utilizar o getter de acerto para qualquer propósito.
    
    '''
    def verifica(self, letras_utilizadas: list(), palavra_atual: str()):
        if self.__letra not in letras_utilizadas:
            if self.__letra in palavra_atual:
                self.__acertou = True
                self.__repetida = False
            else:
                self.__acertou = False
                self.__repetida = False
        else:
            self.__repetida = True
        
        return
        
    def get_letra(self): #Retorna a letra já testada
        return self.__letra
    
    def get_acerto(self): #Retorna se a letra está contida na palavra atual
        return self.__acertou
    
    def get_repetida(self): #Retorna se a letra já foi proposta pelo usuário anteriormente
        return self.__repetida
    