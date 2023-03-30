from models import *

bacground = transform.scale(image.load("20230227084312.png"), WINDOW_SIZE)

player1= Player("p.png", Sprite_Size[0], WINDOW_SIZE[1] - Sprite_Size[1], 5, Sprite_Size)   
player2 = Player("ufo.png", WINDOW_SIZE[0] - Sprite_Size[0] * 2, 0, 5,  Sprite_Size) 

ball = GameSprite("asteroid.png", WINDOW_SIZE[0] / 2 - Ball_Size[0] / 2, WINDOW_SIZE[1] / 2 - Ball_Size[1] / 2, 0, Ball_Size)
speed_x = 3
speed_y = 3


clock = time.Clock()

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:

        window.blit(bacground, (0, 0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y <= 0 or ball.rect.y >= WINDOW_SIZE[1] - ball.rect.height:
            speed_y *= -1.1

        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            speed_x *= -1.1

        ball.reset()
        player1.reset()
        player2.reset()


        player1.move("LEFT")
        player2.move("RIGHT")

        clock.tick(FPS)
        display.update()