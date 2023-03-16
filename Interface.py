class Interface():
    
    def __init__(self):
        self.__forca = list()
        self.__letras_utilizadas = list()
        self.__tentativa_atual = list()
        
    '''
    Atualiza os dados da interface.
    '''
    def atualiza(self, letras_utilizadas: list(), tentativa_atual: list()):
        #self.__forca = pass Hablitar quando forca estiver pronto
        self.__letras_utilizadas = letras_utilizadas
        self.__tentativa_atual = tentativa_atual
        return
    
    '''
    Mostra na tela a forca, as letras utilizadas e a tentativa atual.
    '''
    def inicializa(self):
        #print(self.__forca) Hablitar quando forca estiver pronto
        print(' '.join(self.__tentativa_atual))
        print('Letras já utilizadas:' + ' '.join(self.__letras_utilizadas))
        print('Digite uma letra:')
        return