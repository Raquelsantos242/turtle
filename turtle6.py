import turtle

turtle.bgcolor('black') #cor de fundo
turtle.color('#783c00') #cor da linha
turtle.shape('turtle') #escolhe o ícone que faz o desenho da tela


turtle.setup(640,480)
turtle.speed('fastest')

for y in range(-200,201,20):
    turtle.penup()
    turtle.goto(-300,y)
    turtle.pendown()
    turtle.forward(600)
    turtle.left(90)
for x in range(-300,301,20):
    turtle.penup()
    turtle.goto(x,-200)
    turtle.pendown()
    turtle.forward(400)