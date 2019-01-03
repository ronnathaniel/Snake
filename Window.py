class Window:
    def __init__(self):
            self.pygame_setup()
            self.snake = Snake()
            self.food = Food()
            self.main()

    def pygame_setup(self):
        py.init()
        self.screen = py.display.set_mode((400, 400))
        # creates GUI
        py.display.set_caption("")

    def draw_background(self):
        surface = self.screen
        color = (0, 0, 0)
        rect = py.Rect(0, 0, 400, 410)
        py.draw.rect(surface, color, rect)
        for i in range(21):
            py.draw.line(self.screen, (255,255, 255), (20*i, 0), (20*i, 400))
            py.draw.line(self.screen, (255, 255,255), (0, 20*i), (400, 20*i))

    def draw_snake(self):
        surface = self.screen
        color = (0, 255, 0)
        for spot in self.snake.stack:
            rect = py.Rect(spot[0]+1, spot[1]+1, 19, 19)
            py.draw.rect(surface, color, rect)

    def draw_food(self):
        surface = self.screen
        color = (255, 0, 0)
        rect = py.Rect(self.food.x+1, self.food.y+1, 19, 19)
        py.draw.rect(surface, color, rect)

    def key_press(self):
        press = py.key.get_pressed()
        if press[py.K_UP] and self.snake.y_speed <= 0:
            self.snake.move_up()
        if press[py.K_DOWN] and self.snake.y_speed >= 0:
            self.snake.move_down()
        if press[py.K_RIGHT] and self.snake.x >= 0:
            self.snake.move_right()
        if press[py.K_LEFT] and self.snake.x_speed <= 0:
            self.snake.move_left()

    def events(self):
        if not 0 <= self.snake.x <= 380 or not 0 <= self.snake.y <= 380:
            time.sleep(0.08)
            print("Congrats! Your score was %d!" % len(self.snake.stack))
            self.__init__()

        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.snake.eat()
            self.food.__init__()
            if (self.food.x, self.food.y) in self.snake.stack:
                self.food.__init__()

    def main(self):
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    break
            if py.key.get_pressed()[py.K_ESCAPE]:
                break

            py.display.flip()
            self.key_press()
            self.snake.update()
            self.draw_background()
            self.draw_snake()
            self.draw_food()
            self.events()

            py.time.Clock().tick(15 + len(self.snake.stack)/1.5)


if __name__ == "__main__":
    import pygame as py
    from snaek.Snake import Snake
    from snaek.Food import Food
    import time
    Window()
