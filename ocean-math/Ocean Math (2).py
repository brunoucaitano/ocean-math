

import pygame, random, json
pygame.init()
#Menu Inicial

# Imagens da tela inicial
imgFundo = pygame.image.load("./imagens/imgfundo.png")
imgJogar = pygame.image.load("./imagens/JOGAR.png")

# Janela da tela inicial
LARGURAJANELA = 900
ALTURAJANELA = 700
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Ocean Math")
janela.blit(imgFundo, [0, 0])
janela.blit(imgJogar, [338, 260])



# Bordas das janela inicial
BORDAESQUERDA = 0
BORDADIREITA = LARGURAJANELA
BORDASUPERIOR = 0
BORDAINFERIOR = ALTURAJANELA


# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# Textos
fonte = pygame.font.Font(None, 24)
texto = fonte.render("Todos os direitos reservados © 2018", True, PRETO)
janela.blit(texto, [596, 680])
texto = fonte.render("Bruno, Blenda, Debora & Hemersson", True, PRETO)
janela.blit(texto, [10, 10])


# Atualização da tela
pygame.display.update()
pygame.image.get_extended()

# Som
#pygame.mixer.music.load("./audios/menuinicial.mp3")
#pygame.mixer.music.play(-1, 0.0)

continuar = True
# Game loop
deve_continuar = True
loop = True
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
            continuar = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                deve_continuar = False
                continuar = F
                alse
        if event.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pos()[0] >= 380) and  (pygame.mouse.get_pos()[0] <= 479) and (pygame.mouse.get_pos()[1] >= 200) and  (pygame.mouse.get_pos()[1] <= 257):
            deve_continuar = False
        if event.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pos()[0] >= 330) and  (pygame.mouse.get_pos()[0] <= 479) and (pygame.mouse.get_pos()[1] >= 300) and  (pygame.mouse.get_pos()[1] <= 357):
            deve_continuar = False
            continuar = False
        if event.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pos()[0] >= 330) and  (pygame.mouse.get_pos()[0] <= 479) and (pygame.mouse.get_pos()[1] >= 300) and  (pygame.mouse.get_pos()[1] <= 357):
            deve_continuar = False
            continuar = False
            loop = False


#Jogo

# Função peixe
def adicionarPeixe(peixe, peixes):
    coluna = random.randint(0, LARGURA_JANELA - peixe.get_width())
    linha = random.randint(150, ALTURA_JANELA - peixe.get_height())
    velocidade = random.randint(1, 7)
    peixe = {
        'rect': pygame.Rect(coluna, linha, peixe.get_width(), peixe.get_height()),
        'imagem': peixe,
        'velocidade': [velocidade],
        'correta' : False
    }
    peixes.append(peixe)
        
def apagar_peixe(peixe):
    del peixes[peixe]
    
    
def mover_peixe(figura):
    figura["rect"].x += figura["velocidade"][0]

def capturar(posicao, peixe):
    if (posicao[0] >= peixe["rect"].left) and (posicao[0] <= peixe["rect"].right):
        if (posicao[1] >= peixe["rect"].top ) and (posicao[1] <= peixe["rect"].bottom):
            return True
    return False


def colocarTexto(texto,fonte,cortexto,janela,x,y):
    objTexto = fonte.render(texto, True, cortexto)
    rectTexto= objTexto.get_rect()
    rectTexto.topleft=(x,y)
    janela.blit(objTexto,rectTexto)

        

# Paleta de cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0,0,245)
VERDE = (0,255,0)



# Tamanho da janela do jogo
LARGURA_JANELA, ALTURA_JANELA = (900, 700)

# Bordas das janela
BORDA_ESQUERDA = 0
BORDA_DIREITA = LARGURA_JANELA
BORDA_SUPERIOR = 0
BORDA_INFERIOR = ALTURA_JANELA

# Inicializando o pygame
pygame.init()

# criando um objeto pygame.time.Clock
relogio = pygame.time.Clock()


# Representando as questões

q0 = {
    'pergunta' : '4',
    'respostas': ['2+5', '2x4', '6-2', '18/2'],
    'correta': '6-2'
}

q1 = {
    'pergunta' : '9',
    'respostas': ['3+3', '3x3', '12-4', '12/4'],
    'correta': '3x3'
}

q2 = {
    'pergunta' : '5',
    'respostas': ['2+5', '2x4', '7-2', '14/2'],
    'correta': '7-2'
}

questoes = [q0, q1, q2]

fonte = pygame.font.Font(None, 50)

# Criando a janela
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Ocean Math")

acertos = 0


# Imprimir o texto
fonte = pygame.font.SysFont(None, 48)

# Carregando Background

img_cenario = pygame.image.load("./imagens/FUNDO.png")
imgPeixe1 = pygame.image.load("./imagens/peixe1.png")
imgPeixe2 = pygame.image.load("./imagens/peixe2.png")
imgPeixe3 = pygame.image.load("./imagens/peixe3.png")
imgPeixe4 = pygame.image.load("./imagens/peixe4.png")
imgPeixe5 = pygame.image.load("./imagens/peixe5.png")
imgfechar2 = pygame.image.load("./imagens/fechar2.png")

# musica de fundo
#pygame.mixer.music.load('./audios/mar.mp3')
#pygame.mixer.music.play(-1, 0.0)


peixes = []
i = 0
peixe_certo = False
questaoAtual = random.randint(0, 2)
continuar = True
# Game Loop
while continuar:

    # Checar os eventos
    for evento in pygame.event.get():
        # Checar evento de fechar a janela
        if evento.type == pygame.QUIT:
            continuar = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            peixe_certo = capturar(evento.pos, peixe)
            if peixe_certo:
                acertos = acertos +1
                questaoAtual = random.randint(0,2)
    
    if (len(peixes) < 3):
        p = random.randint(1, 5)        
        if p == 1:
            adicionarPeixe(imgPeixe1, peixes);
        elif p == 2:
            adicionarPeixe(imgPeixe2, peixes);
        elif p == 3:
            adicionarPeixe(imgPeixe3, peixes);
        elif p == 4:
            adicionarPeixe(imgPeixe4, peixes);
        elif p == 5:
            adicionarPeixe(imgPeixe5, peixes);             
       
      
    for peixe in peixes:
        i = peixes.index(peixe)
        mover_peixe(peixe)
        if peixe["rect"].right > BORDA_DIREITA:
            del peixes[i]  
    
    # desenhar o fundo       
    janela.blit(img_cenario, (0,0))

    # desenhar a pontuação
    texto = 'Pontuação: ' + str (acertos)
    colocarTexto(texto,fonte,PRETO,janela,10,10)

    # desenhar o desafio
    texto = 'Número à acertar: ' + questoes[questaoAtual]['pergunta']
    colocarTexto(texto,fonte,PRETO,janela,450,10)
   
    # desenhar peixes na tela      
    i = 0
    for peixe in peixes:
        janela.blit(peixe["imagem"], peixe["rect"])
        texto = questoes[questaoAtual]['respostas'][i]
        colocarTexto(texto,fonte,PRETO,janela,peixe["rect"][0],peixe["rect"][1])
        i= i+1

    # tela final
    if acertos >= 3 :
        continuar = False


    #Atualizar a tela
    pygame.display.update()


    # limitando a ;10 quadros por segundo
    relogio.tick(10)     
        
    

# tela final
# janela

imgFundo2 = pygame.image.load("./imagens/imgfundo2.jpeg")
LARGURAJANELA_ = 900
ALTURAJANELA_ = 700
janela = pygame.display.set_mode((LARGURAJANELA_, ALTURAJANELA_))
pygame.display.set_caption("Ocean Math")
janela.blit(imgFundo2, [0, 0])

# fonte e imagens
fonte = pygame.font.Font(None, 64)
texto = fonte.render("Fim de jogo!", True, PRETO)
janela.blit(texto, [339, 260])
texto = fonte.render("Parabéns, você conseguiu!", True, PRETO)
janela.blit(texto, [210, 310])



# créditos
fonte = pygame.font.Font(None, 24)
texto = fonte.render("Todos os direitos reservados © 2018", True, PRETO)
janela.blit(texto, [596, 680])


# som
#pygame.mixer.music.load('./audios/marfinal.mp3')
#pygame.mixer.music.play(-1, 0.0)

deve_continuar = True
continuar = True

# game loop
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
            continuar = False

            
    # atualizar o jogo
    pygame.display.update()

# Encerrar os módulos do pygame
pygame.quit()


