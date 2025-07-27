from .button import * 
from .list_display import * 
from .draw_down_menu import * 
from .UIconstants import *
import pygame 


def render_main_menu(screen):
    
    pygame.display.set_caption("Algorithm Visualizer")
    
    dropdown_font = pygame.font.Font(None,DROP_DOWN_FONT_SIZE)
    list_elements_font = pygame.font.Font(None ,LIST_FONT_SIZE)
    button_font = font = pygame.font.SysFont("Arial", GEN_ARR_FONT_SIZE)
    
    list_display = ListDisplay(
        ARRAY , LIST_CORDINATES[0] , LIST_CORDINATES[1] ,
        LIST_WIDTH , LIST_HEIGHT , list_elements_font ,
        LIST_BACKGROUND_COLOR , LIST_TEXT_COLOR ,
        LIST_BOARDER_COLOR
        )
    
    dropdown = Dropdown(
        DROPDOWN_COORDINATES[0] , DROPDOWN_COORDINATES[1],
        DROP_DOWN_WIDTH , DROP_DOWN_HEIGHT,
        dropdown_font, DROPDOWN_BOX_COLOR,
        DROPDOWN_HOVER_COLOR , DROPDOWN_TEXT_COLOR , LIST_OF_ALGORITHMS
        )

    generate_arr_button = Button(
        GEN_ARR_COORDINATES[0] , GEN_ARR_COORDINATES[1] ,
        GEN_ARR_WIDTH , GEN_ARR_HEIGHT , GEN_ARR_TEXT ,
        button_font ,GEN_ARR_BG_COLOR , GEN_ARR_TEXT_COLOR
        )
    
    return list_display , dropdown , generate_arr_button 
    
def render_next_button(screen):
    button_font = pygame.font.Font(None, NEXT_BUT_FONT_SIZE)
    
    next_button = Button(
        NEXT_BUT_COORDINATES[0], NEXT_BUT_COORDINATES[1],
        NEXT_BUT_WIDTH, NEXT_BUT_HEIGHT, NEXT_BUT_TEXT,
        button_font, NEXT_BUT_BG_COLOR, NEXT_BUT_TEXT_COLOR,
        NEXT_BUT_BORDER_COLOR
    )
    
    return next_button

def render_play_all_button(screen):
    button_font = pygame.font.Font(None, PLAY_BUT_FONT_SIZE)
    
    play_button = Button(
        PLAY_BUT_COORDINATES[0], PLAY_BUT_COORDINATES[1],
        PLAY_BUT_WIDTH, PLAY_BUT_HEIGHT, PLAY_BUT_TEXT,
        button_font, PLAY_BUT_BG_COLOR, PLAY_BUT_TEXT_COLOR,
        PLAY_BUT_BORDER_COLOR
    )
    
    return play_button

if __name__ == "__main__":
    main()