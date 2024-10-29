import sys
import pygame
from settings import Settings
# create a class to make window for game
class alian_invasion:
    # create the behavior and assets of game
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode(self.setting)
        pygame.display.set_caption("ALIAN INVASION")
        self.clock=pygame.time.Clock()
        self.bg_color=(230,140,230)

    def run_game(self):
        # start the main loop for the game
        while True:
            # watch the mouse and keyboard
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                   sys.exit()
            # make draw the screen visible
            pygame.display.flip()
            # pygame.clock.tick()
            self.screen.fill(self.bg_color)

if __name__ == '__main__':
    # make a game instance and run the game
    ai=alian_invasion()
    ai.run_game()
