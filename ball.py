import turtle
import random


class Ball:
    def __init__(self, xpos, ypos, vx, vy, ball_color, canvas_width,
                 canvas_height, ball_radius, num_balls):
        self.x = xpos
        self.y = ypos
        self.vx = vx
        self.vy = vy
        self.color = ball_color
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.size = ball_radius
        self.num_balls = num_balls

    def draw_circle(self, i):
        """
        draw a circle of radius equals to size at x, y coordinates and paint it
        with color
        parameter i is the index of the circle
        :return:
        """
        turtle.penup()
        turtle.color(self.color[i])
        turtle.fillcolor(self.color[i])
        turtle.goto(self.x[i], self.y[i])
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_circle(self, i):
        """
        update the x, y coordinates of ball i with velocity in the x (vx) and
        y (vy) components.
        :param i:
        :return:
        """
        self.x[i] += self.vx[i]
        self.y[i] += self.vy[i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.x[i] + self.vx[i]) > (self.canvas_width - self.size):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.y[i] + self.vy[i]) > (self.canvas_height - self.size):
            self.vy[i] = -self.vy[i]

    def initilizing(self):
        """
        create random number of balls, num_balls, located at random positions
        within the canvas; each ball has a random velocity value in the x and
        y direction and is painted with a random color
        :return:
        """
        for i in range(self.num_balls):
            self.x.append(random.randint(-1*self.canvas_width + self.size, self.canvas_width - self.size))
            self.y.append(random.randint(-1*self.canvas_height + self.size, self.canvas_height - self.size))
            self.vx.append(random.randint(1, 0.01*self.canvas_width))
            self.vy.append(random.randint(1, 0.01*self.canvas_height))
            self.color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))