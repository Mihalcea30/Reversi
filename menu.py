import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = SCREEN_WIDTH // COLS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
FONT_SIZE = 40

# The Start Menu

class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.difficulty_levels = ['Easy', 'Medium', 'Hard']  # List of difficulty levels
        self.current_difficulty_index = 0  # Index of the current difficulty level
        self.symbol_options = ['White', 'Black']  # List of symbol options
        self.current_symbol_index = 0  # Index of the current symbol option

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_button(self, text, font, color, x, y, width, height):
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, color, button_rect)
        self.draw_text(text, font, BLACK, x + width / 2, y + height / 2)

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
                        return self.difficulty_levels[self.current_difficulty_index], self.symbol_options[self.current_symbol_index]  # Return to start the game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if difficulty_button.collidepoint(event.pos):
                        self.current_difficulty_index = (self.current_difficulty_index + 1) % len(self.difficulty_levels)
                        print("Difficulty changed to:", self.difficulty_levels[self.current_difficulty_index])
                    elif symbol_button.collidepoint(event.pos):
                        self.current_symbol_index = (self.current_symbol_index + 1) % len(self.symbol_options)
                        print("Symbol changed to:", self.symbol_options[self.current_symbol_index])

            # Fill the background
            self.screen.fill(WHITE)

            # Draw title
            self.draw_text("Reversi", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

            # Draw instructions
            self.draw_text("Press ENTER to start", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

            # Draw difficulty button
            difficulty_button_width = 400
            difficulty_button_height = 50
            difficulty_button_x = SCREEN_WIDTH // 2 - difficulty_button_width // 2
            difficulty_button_y = SCREEN_HEIGHT // 2 + 50
            self.draw_button("Difficulty: " + self.difficulty_levels[self.current_difficulty_index], font, GREY, difficulty_button_x, difficulty_button_y, difficulty_button_width, difficulty_button_height)

            # Draw symbol button
            symbol_button_width = 400
            symbol_button_height = 50
            symbol_button_x = SCREEN_WIDTH // 2 - symbol_button_width // 2
            symbol_button_y = SCREEN_HEIGHT // 2 + 150
            self.draw_button("Symbol: " + self.symbol_options[self.current_symbol_index], font, GREY, symbol_button_x, symbol_button_y, symbol_button_width, symbol_button_height)

            # Define button rectangles for collision detection
            difficulty_button = pygame.Rect(difficulty_button_x, difficulty_button_y, difficulty_button_width, difficulty_button_height)
            symbol_button = pygame.Rect(symbol_button_x, symbol_button_y, symbol_button_width, symbol_button_height)

            # Update the display
            pygame.display.flip()



