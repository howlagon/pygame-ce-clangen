import pygame_gui, pygame
import traceback
from textwrap import dedent

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((400, 200))
manager = pygame_gui.UIManager((400, 200))

display.fill((200, 200, 200))

textbox = pygame_gui.elements.UITextBox(dedent("""\
                                        Img src alpha test
                                        <img src='spacer_clipstudio.png' /> <img src='button_clipstudio.png' />
                                        <img src='spacer_firealpaca.png' /> <img src='button_firealpaca.png' />"""),
                                        pygame.Rect((50, 25), (300, 150)), 
                                        manager=manager)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: exit(0)
            manager.process_events(event)
        manager.draw_ui(display)
        pygame.display.update()
        manager.update(1/30)
        clock.tick(30)

try:
    main()
except KeyboardInterrupt:
    exit(0)
except Exception as e:
    print(traceback.format_exc())
    exit(1)