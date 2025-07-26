import pygame 
from .button import * 
import random
from .UIconstants import ELEMENT_SPACING
class ListDisplay:
    def __init__(self, data, x, y, box_width, box_height, font, bg_color, text_color, border_color):
        self.data = data
        self.x = x
        self.y = y
        self.box_width = box_width
        self.box_height = box_height
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.border_color = border_color
        self.buttons = self._create_buttons()

    def _create_buttons(self):
        buttons = []
        for i, item in enumerate(self.data):
            btn_x = self.x + i * (self.box_width + ELEMENT_SPACING)
            button = Button(btn_x, self.y, self.box_width, self.box_height, str(item), self.font, self.bg_color, self.text_color, self.border_color)
            buttons.append(button)
        return buttons

    def draw(self, screen):
        for i,button in enumerate(self.buttons):
            button.changeText(str(self.data[i]))
            button.draw(screen)

    def get_clicked_index(self, pos):
        for i, button in enumerate(self.buttons):
            if button.is_clicked(pos):
                return i
        return None
    def generate_arr(self):
        for i in range(len(self.data)):
            self.data[i] = random.randint(0,20)