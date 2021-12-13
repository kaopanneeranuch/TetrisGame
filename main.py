import turtle
import time
import random

wn = turtle.Screen()
wn.title("TETRIS")
wn.setup(width=400, height=600)
wn.bgcolor("black")
wn.tracer(0)


class Shape():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 7)
        #block
        square = [[1,1],
                  [1,1]]

        line = [[1,1,1,1]]


        left_l = [[1,0,0],
                  [1,1,1]]

        right_l = [[0,0,1],
                   [1,1,1]]

        left_s = [[1,1,0],
                  [0,1,1]]

        right_s = [[0,1,1],
                   [1,1,0]]

        t = [[0,1,0],
             [1,1,1]]

        shapes = [square, line, left_l, right_l, left_s, right_s, t]
        self.shape = random.choice(shapes)

        self.height = len(self.shape)
        self.width = len(self.shape[0])

    
    def move_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.erase_shape(grid)
                self.x -= 1

    def move_right(self, grid):
        if self.x < 12 - self.width:
            if grid[self.y][self.x + self.width] == 0:
                self.erase_shape(grid)
                self.x += 1

    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    grid[self.y + y][self.x + x] = self.color

    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    grid[self.y + y][self.x + x] = 0

    def can_move(self, grid):
        result = True
        for x in range(self.width):
            #check if bottom is 1
            if(self.shape[self.height-1][x] == 1):
                if(grid[self.y + self.height][self.x + x] != 0):
                    result = False

        return result

    def rotate(self, grid):
        #erase the original shape
        self.erase_shape(grid)
        rotated_shape = []
        for x in range (len(self.shape[0])):
            new_row = []
            for y in range(len(self.shape)-1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)
        
        right_side = self.x + len(rotated_shape[0])
        if right_side < len(grid[0]):
            self.shape = rotated_shape
            #update height & width
            self.height = len(self.shape)
            self.width = len(self.shape[0])



grid = [
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       ]

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.shape("square")
pen.setundobuffer(None)


def draw_grid(pen, grid):
    pen.clear()
    top = 245
    left = -115

    colors = ["black", "brown", "red", "orange", "yellow", "purple", "blue", "green"]

    for y in range (len(grid)):
        for x in range (len(grid[0])):
            screen_x = left + (x * 20)
            screen_y = top - (y *20)
            color = colors[grid[y][x]]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()

def check_grid(grid):
    #Check if row is full
    y = 23
    while y > 0:
        is_full = True
        for x in range(0, 12):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break

        if is_full:
            global score
            score += 1
            draw_score(pen, score)
            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x] = grid[copy_y-1][copy_x] #if is_full the line is gone

def draw_score(pen, score):
    pen.hideturtle()
    pen.color("white")
    pen.goto(80,250)
    pen.write("Score: {}".format(score), font=("Arial", 15, "normal"))


# Create the basic shape for the start  of the game
shape = Shape()

#Put shape in to grid
grid[shape.y][shape.x] = shape.color


draw_grid(pen, grid)


#keyboard binding
wn.listen()
wn.onkey(lambda: shape.move_left(grid), "Left")
wn.onkey(lambda: shape.move_right(grid), "Right")
wn.onkey(lambda: shape.rotate(grid), "space")

score = 0

#Main
while True:
    wn.update()

    #Move the shape down
    #fist row
    if shape.y == 23 - shape.height + 1:
        shape = Shape()
        check_grid(grid)
    elif shape.can_move(grid):
        #erase the current shape
        shape.erase_shape(grid)
        #move the shape by 1
        shape.y += 1
        #draw the shape again
        shape.draw_shape(grid)

        
    else:
        shape = Shape()
        check_grid(grid)
        
    draw_grid(pen, grid)
    draw_score(pen, score)

    time.sleep(0.1)
wn.mainloop()
