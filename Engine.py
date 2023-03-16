class Engine():
    
    def __init__(self):
        self.__acertou = bool()
        self.__repetida = bool()
        self.__letra = str
        self.__letras_multiplas = bool()
        
    '''
    Verifica se a letra já foi utilizada, e se a letra está contida na palavra ou não.
    
    Obs: Se a letra estiver repetida a função de verificação não verifica se letra
         está ou não na palavra atual, ela apenas altera o atributo "self.__repetida"
         para "True", e por padrão se apenas classificamos uma variável como boolena
         em python(como no __init__ dessa classe) ela tem valor base "False", logo
         deve-se ter cuidado para checar se a letra está repetida ou não antes
         de utilizar o getter de acerto para qualquer propósito.
    
    '''
    def verifica(self, letra: str(), letras_utilizadas: list(), palavra_atual: str()):
        self.__letra = letra
        if len(self.__letra) > 1: self.__letras_multiplas = True
        if self.__letra not in letras_utilizadas:
            self.__repetida = False
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
    
    def get_letras_multiplas(self): # Retorna se o jogador digitou mais de uma letra
        return self.__letras_multiplas
    