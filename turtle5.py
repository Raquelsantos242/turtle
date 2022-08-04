import turtle

turtle.bgcolor('black') #cor de fundo
turtle.color('#783c00') #cor da linha
turtle.shape('turtle') #escolhe o ícone que faz o desenho da tela


def desenha_quadrado(l):
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(l)
    #desenha os 12 quadrados rotacionados
for i in range(12):
    #desenha um quadrado
    desenha_quadrado(100)
    #rotaciona 120 graus
    turtle.right(120)