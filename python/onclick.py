import turtle

RADIUS = 2

def func(x, y):
    print("clicked:", x, y)

turtle.onscreenclick(func)

for _ in range(360):
    turtle.forward(1)
    turtle.right(1)

turtle.mainloop()
