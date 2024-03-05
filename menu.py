import pygame
import sys

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ROWS = 8
COLS = 8
SQUARE_SIZE = SCREEN_WIDTH // COLS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
FONT_SIZE = 40

# the Start Menu

class Menu:
  def __init__(self):
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  def draw_text(self, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    self.screen.blit(text_surface, text_rect)

  def start_menu(self):
    # Font
    font = pygame.font.Font(None, FONT_SIZE)

    # Main menu loop
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            return  # Return to start the game

      # Fill the background
      self.screen.fill(WHITE)

      # Draw title
      self.draw_text("Reversi", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

      # Draw instructions
      self.draw_text("Press ENTER to start", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

      # Update the display
      pygame.display.flip()

