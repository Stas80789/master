from pygame import *
WINDOW_SIZE = (700, 500)
Sprite_Size = (20, 100)
Ball_Size = (30, 35)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
BlacK = (0, 0, 0)
FPS = 60

window = display.set_mode(WINDOW_SIZE)
font.init()
font = font.Font(None, 18)

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x_pos, y_pos, speed, size):
        super().__init__()
        self.image = transform.scale(image.load(image_name), size)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self, direction):
        keys = key.get_pressed()

        if direction == "LEFT":
            if keys[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < WINDOW_SIZE[1] - Sprite_Size[1]:
                self.rect.y += self.speed
        elif direction == "RIGHT":             
            if keys[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < WINDOW_SIZE[1] - Sprite_Size[1]:
                self.rect.y += self.speed