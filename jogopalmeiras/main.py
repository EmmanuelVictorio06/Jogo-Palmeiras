# Bibliotecas
import pygame

# Inicialização
pygame.init()
pygame.font.init()

# Tela
tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Jogo do Palmeiras')
fonte = pygame.font.Font(None, 40)

# Imagens
largura_tela, altura_tela = tela.get_size()
inic = pygame.image.load(r"C:\Users\Wallace PUC\Downloads\JogoDet\jogopalmeiras\assets\capa.png")  #Inserir caminho da pasta extraída
introduc = pygame.image.load(r"C:\Users\Wallace PUC\Downloads\JogoDet\jogopalmeiras\assets\introducao.png") #Inserir caminho da pasta extraída
fatos = pygame.image.load(r"C:\Users\Wallace PUC\Downloads\JogoDet\jogopalmeiras\assets\fatos.png") #Inserir caminho da pasta extraída
regra = pygame.image.load(r"C:\Users\Wallace PUC\Downloads\JogoDet\jogopalmeiras\assets\regras.png") #Inserir caminho da pasta extraída
proposicoe = pygame.image.load(r"C:\Users\Wallace PUC\Downloads\JogoDet\jogopalmeiras\assets\proposicoes.png") #Inserir caminho da pasta extraída
premisa = pygame.image.load(r"C:\Users\Wallace PUC\Downloads\JogoDet\jogopalmeiras\assets\culpado.png") #Inserir caminho da pasta extraída
final = pygame.image.load(r"C:\Users\Wallace PUC\Downloads\JogoDet\jogopalmeiras\assets\final.png") #Inserir caminho da pasta extraída

# Dimenção imagem
inicio = pygame.transform.scale(inic, (largura_tela, altura_tela))
regras = pygame.transform.scale(regra, (largura_tela, altura_tela))
introducao = pygame.transform.scale(introduc, (largura_tela, altura_tela))
fatos = pygame.transform.scale(fatos, (largura_tela, altura_tela))
proposicoes = pygame.transform.scale(proposicoe, (largura_tela, altura_tela))
premissas = pygame.transform.scale(premisa, (largura_tela, altura_tela))
final = pygame.transform.scale(final, (largura_tela, altura_tela))

# Variaveis
user_text = ''
input_rect = pygame.Rect(200, 200, 140, 32)
color_active = (135, 206, 235)
color_passive = (177, 188, 85)
branco = (255, 255, 255)
preto = (0, 0, 0)
active = False
LEFT = 1
RIGHT = 3
input_rect.x += 355
input_rect.y += 425
input_rect.width *= 2
input_rect.height *= 2

# Cenas
loop = True
cena = "inicial"

while loop:
    if cena == "inicial":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                cena = "regras"

            tela.blit(inicio, (0, 0))

    if cena == "regras":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                cena = "introducao"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "inicial"
            tela.blit(regras, (0, 0))

    elif cena == "introducao":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                cena = "fatos"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "regras"
        tela.blit(introducao, (0, 0))

    elif cena == "fatos":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                cena = "proposicoes"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "introducao"
        tela.blit(fatos, (0, 0))

    # Proposicoes
    elif cena == "proposicoes":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                cena = "premissas"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "fatos"
            tela.blit(proposicoes, (0, 0))

    # Premissas
    elif cena == "premissas":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "proposicoes"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user_text == "F":
                    cena = "final"
               
                if event.key == pygame.K_BACKSPACE:
                  
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

            # Fundo
            tela.blit(premissas, (0, 0))
            if active:
                color = color_active
            else:
                color = color_passive

            # Desenha a caixa de resposta
            pygame.draw.rect(tela, color, input_rect)

            text_surface = fonte.render(user_text, True, (0))

            # Desenha o texto
            tela.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

            # Limitar o texto dentro da caixa de resposta
            input_rect.w = max(100, text_surface.get_width() + 10)

    elif cena == "final":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
        tela.blit(final, (0, 0))

    pygame.display.flip()
