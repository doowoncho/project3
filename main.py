import turtle

turtle.bgcolor("grey")
turtle.setup(600,600)
turtle.shape("turtle")

screen = turtle.Screen()
sally = turtle.Turtle()

def star(color, length):

  sally.fillcolor(color)
  sally.begin_fill()

  corners = 0
  while corners < 5:
    sally.forward(length)
    sally.right(144)
    corners += 1

  sally.end_fill()


def triangle():
  sally.fillcolor(color)
  sally.begin_fill()

  corners = 0
  while corners < 3:
    sally.forward(length)
    sally.right(120)
    corners += 1

  sally.end_fill()
  
def circle():
  print("draw circle!")

shape = input("give me a shape: ")
color = input("give me a color: ")
length = int(input("give me a length: "))

if shape == "star":
  star(color, length)
elif shape =="triangle":
  triangle()
elif shape == "circle":
  circle()
