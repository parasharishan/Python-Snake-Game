from turtle import Turtle


class Snake:
    def __init__(self):
        x = 0
        y = 0
        self.snake_segments = []
        for _ in range(0, 3):
            self.add_segment(x, y)
            x -= 20
        self.head = self.snake_segments[0]

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def add_segment(self, x, y):
        new_segment = Turtle(shape="square")
        new_segment.speed("slowest")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(x, y)
        self.snake_segments.append(new_segment)

    def elongate(self):
        x_loc_second_last_segment = self.snake_segments[len(self.snake_segments) - 1].xcor()
        y_loc_second_last_segment = self.snake_segments[len(self.snake_segments) - 1].ycor()
        self.add_segment(x_loc_second_last_segment, y_loc_second_last_segment)
        # not necessary as animation will take care of it
        # if self.head.heading() == 90:
        #     x = x_loc_second_last_segment
        #     y = y_loc_second_last_segment - 20
        #     self.add_segment(x, y)
        #
        # if self.head.heading() == 270:
        #     x = x_loc_second_last_segment
        #     y = y_loc_second_last_segment + 20
        #     self.add_segment(x, y)
        #
        # if self.head.heading() == 0:
        #     x = x_loc_second_last_segment - 20
        #     y = y_loc_second_last_segment
        #     self.add_segment(x, y)
        #
        # if self.head.heading() == 180:
        #     x = x_loc_second_last_segment + 20
        #     y = y_loc_second_last_segment
        #     self.add_segment(x, y)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


