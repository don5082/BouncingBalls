import Ball
import pygame

pygame.init()
W, H = 800, 800
WHITE = (255,255,255)

TIME_SCALE = 8  # 5 times speed

COLLISION_ENERGY_LOSS = 5  # speed lost due to friction

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("My Physics Engine Render")
clock = pygame.time.Clock()



def simulate():
    running = True
    balls = []
    ball = Ball.Ball(W//2, 100, 10,0,0)
    balls.append(ball)

    while(running):
        # dt = seconds since last frame
        dt = clock.tick(120) / 1000.0  # caps to ~120 FPS, returns milliseconds
        dt *= TIME_SCALE

        for ball in balls:
            ball.simulate(dt)

        screen.fill((0, 0, 0))
        for ball in balls:
            ball.draw(screen)

        pygame.display.flip()

        # ----------------------------
        # Input / window events
        # ----------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    return


if __name__ == "__main__":
    simulate()