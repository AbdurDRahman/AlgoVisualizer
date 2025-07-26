import pygame 

class Button:
    def __init__(self , x , y , width , height , text , font , background_color , text_color , border_color = None):
        
        self.rect = pygame.Rect(x,y,width,height)
        self.text = text 
        self.font = font 
        self.background_color = background_color 
        self.text_color = text_color 
        self.border_color = border_color 

    def draw(self , screen):
        
        if self.border_color is None : pygame.draw.rect(screen , self.background_color , self.rect)
        else:   pygame.draw.rect(screen, self.border_color, self.rect, 2)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def changeText(self,text):
        self.text = text 