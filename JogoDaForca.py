from BancoDePalavras import BancoDePalavras
from Engine import Engine
from Interface import Interface
from Status import Status
from Boneco import Boneco

win = False

banco = BancoDePalavras()
palavra = banco.palavra_aleatoria() #Escolhe uma palavra aleatória do banco de palavras

status = Status(palavra)
engine = Engine()
interf = Interface()
boneco = Boneco()

while status.get_qtd_erros() < 6:
    interf.atualiza(boneco, status.get_letras_utilizadas(), status.get_tentativa_atual())
    interf.inicializa()
    letra_in = input()
    
    engine.verifica(letra_in, status.get_letras_utilizadas(), status.get_palavra_oculta())

    while engine.get_repetida() == True:
        letra_in = input('Digite uma letra não repetida:')
        engine.verifica(letra_in, status.get_letras_utilizadas(), status.get_palavra_oculta())
    
    if engine.get_letras_multiplas() == True: 
        print('Digite apenas uma letra por vez!')
    else:
        erros = status.atualiza(engine.get_letra(), engine.get_acerto())
        boneco.atualizar_forca(erros)
    
    if ' '.join(status.get_tentativa_atual()).replace(' ', '') == status.get_palavra_oculta():
        win = True
        break
    
if win == True:
    print('Parabéns, você ganhou!')
else:
    boneco.atualizar_forca(6)
    print(boneco.desenhar())
    print('Fim de jogo!')
print(f'A palavra era {palavra.capitalize()}')
    
    
    
    
