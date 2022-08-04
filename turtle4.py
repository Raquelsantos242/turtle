import turtle

turtle.bgcolor('black') #cor de fundo
turtle.color('#783c00') #cor da linha
turtle.shape('turtle') #escolhe o ícone que faz o desenho da tela

N = int(input("Entre com o valor de N: "))
cont = 0

while cont < N:
    cont += 1
    turtle.forward(cont)
    turtle.left(90)
    
turtle.exitonclick()