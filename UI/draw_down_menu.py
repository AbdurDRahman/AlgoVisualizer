import pygame

class Dropdown:
    def __init__(self, x, y, width, height, font, main_color, hover_color, text_color, options):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = main_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = font
        self.options = options
        self.selected_index = None
        self.active = False

    def draw(self, screen):
        # Draw the main box
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, self.text_color, self.rect, 2)

        # Draw the selected text
        if self.selected_index is None : selected_text = self.font.render("--select--" , True , self.text_color)
        else: selected_text = self.font.render(self.options[self.selected_index], True, self.text_color)
        screen.blit(selected_text, (self.rect.x + 10, self.rect.y + 5))

        # Draw dropdown options if active
        if self.active:
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height,
                                          self.rect.width, self.rect.height)
                pygame.draw.rect(screen, self.hover_color if option_rect.collidepoint(pygame.mouse.get_pos()) else self.color, option_rect)
                pygame.draw.rect(screen, self.text_color, option_rect, 2)
                option_text = self.font.render(option, True, self.text_color)
                screen.blit(option_text, (option_rect.x + 10, option_rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            elif self.active:
                for i in range(len(self.options)):
                    option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height,
                                              self.rect.width, self.rect.height)
                    if option_rect.collidepoint(event.pos):
                        self.selected_index = i
                        self.active = False
                        break
                else:
                    self.active = False

    def get_selected(self):
        if self.selected_index is None: return None 
        return self.options[self.selected_index]
