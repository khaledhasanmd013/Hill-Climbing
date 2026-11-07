import math

class Environment:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def get_height(self, x):
        return self.screen_height - 150 + int(math.sin(x * 0.01) * 50) + int(math.sin(x * 0.005) * 30)

    def draw(self, screen):
        for x in range(0, self.screen_width, 2):
            y = self.get_height(x)
            screen.set_at((x, y), (0, 255, 0))
            for fill_y in range(y + 1, self.screen_height):
                if fill_y % 5 == 0:
                    screen.set_at((x, fill_y), (34, 139, 34))
                  
