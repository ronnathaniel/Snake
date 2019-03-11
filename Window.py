class Window:
    def __init__(self):
            self.pygame_setup()
            self.snake = Snake()
            self.food = Food()
            self.main()

    def pygame_setup(self):
        pg.init()
        self.screen = pg.display.set_mode((400, 400))
        # creates GUI
        pg.display.set_caption("")

    def draw_background(self):
        surface = self.screen
        color = (0, 0, 0)
        rect = pg.Rect(0, 0, 400, 410)
        pg.draw.rect(surface, color, rect)
        for i in range(21):
            pg.draw.line(self.screen, (255,255, 255), (20*i, 0), (20*i, 400))
            pg.draw.line(self.screen, (255, 255,255), (0, 20*i), (400, 20*i))

    def draw_snake(self):
        surface = self.screen
        color = (0, 255, 0)
        for spot in self.snake.stack:
            rect = pg.Rect(spot[0]+1, spot[1]+1, 19, 19)
            pg.draw.rect(surface, color, rect)

    def draw_food(self):
        surface = self.screen
        color = (255, 0, 0)
        rect = pg.Rect(self.food.x+1, self.food.y+1, 19, 19)
        pg.draw.rect(surface, color, rect)

    def key_press(self):
        press = pg.key.get_pressed()
        if (press[pg.K_UP] or press[pg.K_w]) and self.snake.y_speed <= 0:
            self.snake.move_up()
        if (press[pg.K_DOWN] or press[pg.K_s]) and self.snake.y_speed >= 0:
            self.snake.move_down()
        if (press[pg.K_RIGHT] or press[pg.K_d]) and self.snake.x >= 0:
            self.snake.move_right()
        if (press[pg.K_LEFT] or press[pg.K_a]) and self.snake.x_speed <= 0:
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
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    break
            if pg.key.get_pressed()[pg.K_ESCAPE]:
                break

            pg.display.flip()
            self.key_press()
            self.snake.update()
            self.draw_background()
            self.draw_snake()
            self.draw_food()
            self.events()

            pg.time.Clock().tick(15 + len(self.snake.stack)/1.5)


if __name__ == "__main__":
    import pygame as pg
    from snaek.Snake import Snake
    from snaek.Food import Food
    import time
    Window()
