class Status():
    
    def __init__(self, palavra: str):
        self.__palavra_oculta = palavra
        self.__qtd_erros = 0
        self.__letras_utilizadas = list()
        self.__tentativa_atual = list("_" * len(palavra))
    
    def get_palavra_oculta(self):
        return self.__palavra_oculta
    
    def get_qtd_erros(self):
        return self.__qtd_erros
    
    def get_letras_utilizadas(self):
        return self.__letras_utilizadas
    
    def get_tentativa_atual(self):
        return self.__tentativa_atual
    
    def atualiza(self, letra: str, acerto: bool):
        if acerto == True:
            self.__letras_utilizadas.append(letra)
            for i in range(len(self.__palavra_oculta)):
                if self.__palavra_oculta[i] == letra:
                    self.__tentativa_atual[i] = letra
        else:
            self.__letras_utilizadas.append(letra)
            self.__qtd_erros += 1
        return
    
