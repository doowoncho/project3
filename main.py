import turtle

turtle.bgcolor("grey")
turtle.setup(600,600)
turtle.shape("turtle")

screen = turtle.Screen()
sally = turtle.Turtle()

def star():
  print("draw star!")

def triangle():
  print("draw triangle!")

def circle():
  print("draw circle!")

shape = input("give me a shape: ")
# color = input("give me a color: ")
# length = input("give me a length: ")

if shape == "star":
  star()
elif shape =="triangle":
  triangle()
elif shape == "circle":
  circle()