class Snake:
    def __init__(self, *, x=20, y=20):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 20
        self.stack = [(self.x, self.y)]

    def move_up(self):
        self.x_speed = 0
        self.y_speed = -self.speed

    def move_down(self):
        self.x_speed = 0
        self.y_speed = self.speed

    def move_right(self):
        self.x_speed = self.speed
        self.y_speed = 0

    def move_left(self):
        self.x_speed = -self.speed
        self.y_speed = 0

    def update(self):
        self.stack.pop()
        self.x += self.x_speed
        self.y += self.y_speed
        self.stack.insert(0, (self.x, self.y))

    def eat(self):
        self.stack.append((self.x, self.y))


if __name__ == "__main__":
    print("Missing File")
