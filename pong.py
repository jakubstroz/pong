import turtle

STEP = 20
WIDTH = 1920
LENGHT = 1000


window = turtle.Screen()
window.title('Pong')
window.bgcolor('black')
window.setup(width=1920, height=1000)
window.tracer(0)

bumper = turtle.Turtle()
bumper.shape("square")
bumper.shapesize(stretch_wid=10, stretch_len=1)
bumper.color('red')
bumper.penup()
bumper.goto(-WIDTH / 2 + 40,0)
bumper.speed(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(stretch_len=2, stretch_wid=2)
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball_speed_x = 0.2
ball_speed_y = 0.2


def go_up(): #if
    bumper.sety(bumper.ycor() + STEP)

def go_down(): #if
    bumper.sety(bumper.ycor() - STEP)

window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")

while True:
    window.update()
    ball.setx(ball.xcor() + ball_speed_x)
    ball.sety(ball.ycor() + ball_speed_y)
    if WIDTH / 2 < ball.xcor() or ball.xcor() < - WIDTH / 2:
        ball_speed_x *= -1
    if LENGHT / 2 < ball.ycor()  or ball.ycor() <  - LENGHT / 2:
        ball_speed_y *= -1

    if ball.xcor() <= -WIDTH /2 + 70 and ball.ycor() < bumper.ycor() + 100:
        ball_speed_x *= -1
